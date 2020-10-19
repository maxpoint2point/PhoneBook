#!/usr/bin/python
import pymysql
from pymysql.cursors import DictCursor
import httplib2
import apiclient.discovery
from app import config
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials

if __name__ != '__main__':
    exit(-1)

log = open(config.LOGFILE, 'a')

log.write(f'<{datetime.now()}>: Начата синхронизаци\n')

CREDENTIALS_FILE = config.API

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
    range='A2:B200000000',
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

query = "INSERT INTO list (phone, name) VALUES (%s, %s)"
log.write(f'<{datetime.now()}>: Заносим данные в базу\n')

for val in values['values']:
    connection.cursor().execute(query, (val[0], val[1]))

connection.commit()
log.write(f'<{datetime.now()}>: Данные обновлены, коммит транзакции\n')
connection.close()

log.write(f'<{datetime.now()}>: Подключение к базе закрыто.\n')
log.write(f'<{datetime.now()}>: Скрипт завершен\n************\n')
log.close()
