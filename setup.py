from setuptools import setup
import app

setup(
    name='PhoneBook',
    version=app.__version__,
    packages=[
        'cachetools==3.1.1',
        'certifi==2020.6.20',
        'cffi==1.14.3',
        'cryptography==3.1.1',
        'google-api-python-client==1.7.11',
        'google-auth==1.6.3',
        'google-auth-httplib2==0.0.3',
        'httplib2==0.13.1',
        'oauth2client==4.1.3',
        'pyasn1==0.4.6',
        'pyasn1-modules==0.2.6',
        'pycparser==2.20',
        'PyMySQL==0.10.1',
        'requests==2.5.0',
        'rsa==4.0',
        'six==1.12.0',
        'uritemplate==3.0.0',
        'urllib3==1.25.10',
    ],
    url='https://github.com/maxpoint2point/PhoneBook',
    license='',
    author='Максим',
    author_email='maxpoint2point@gmail.com',
    description=''
)
