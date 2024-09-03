import os
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.environ.get('REDIS_HOST')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_HOST = os.environ.get('MYSQL_HOST')
MYSQL_DB = os.environ.get('MYSQL_DB')
