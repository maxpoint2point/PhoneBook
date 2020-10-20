#!/usr/bin/python
import pymysql
import time
from pymysql.cursors import DictCursor
import httplib2
import apiclient.discovery
from app import config
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials


def safe__get(val, idx):
    try:
        return val[idx]
    except IndexError:
        return 'default'


if __name__ != '__main__':
    exit(-1)
start_time = time.time()
log = open(config.LOGFILE, 'a')

log.write(f'<{datetime.now()}>: Начата синхронизаци\n')

CREDENTIALS_FILE = config.API
try:
    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            CREDENTIALS_FILE,
            ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive'])
    except:
        log.write(f'<{datetime.now()}>: Отсутствует файл API ключа\n************\n')
        log.close()
        exit(-1)

    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
    log.write(f'<{datetime.now()}>: Выполняется чтение из Google Sheets\n')
    values = service.spreadsheets().values().get(
        spreadsheetId=config.SPREDSHEET,
        range='A2:C200000000',
        majorDimension='ROWS'
    ).execute()

    log.write(f'<{datetime.now()}>: Данные получены, подключаемся к базе\n')

    try:
        connection = pymysql.connect(
            host=config.HOST,
            user=config.USER,
            password=config.PASSWORD,
            db=config.DB_NAME,
            charset='utf8mb4',
            cursorclass=DictCursor
        )
    except:
        log.write(f'<{datetime.now()}>: Невозможно подключиться к БД\n************\n')
        log.close()
        exit(-1)

    log.write(f'<{datetime.now()}>: Очищаем таблицу\n')

    connection.cursor().execute("TRUNCATE TABLE list")

    query = f"INSERT INTO {config.TABLE_NAME} (phone, name, manager) VALUES (%s, %s, %s)"
    log.write(f'<{datetime.now()}>: Заносим данные в базу\n')

    for val in values['values']:
        connection.cursor().execute(query, (val[0], val[1], safe__get(val, 2)))

    connection.commit()
    log.write(f'<{datetime.now()}>: Данные обновлены, коммит транзакции\n')
    connection.close()

    log.write(f'<{datetime.now()}>: Подключение к базе закрыто.\n')
except Exception as e:
    log.write(f'<{datetime.now()}>: {e} <------\n')
finally:
    log.write(f'<{datetime.now()}>: Скрипт завершен за {time.time() - start_time} секунд\n')
    log.write('************\n')
    log.close()
