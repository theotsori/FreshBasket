#!/usr/bin/python3

import os

# Flask configuration
SECRET_KEY = os.environ.get('APP_SECRET_KEY')

# MySQL configuration
DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_DATABASE = os.environ.get('DB_DATABASE')

# MySQL connection config
db_config = {
    'host': DB_HOST,
    'user': DB_USER,
    'password': DB_PASSWORD,
    'database': DB_DATABASE
}
