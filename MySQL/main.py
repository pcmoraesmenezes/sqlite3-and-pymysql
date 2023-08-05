import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_HOST = os.getenv('MYSQL_HOST')

connection = pymysql.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,  # type: ignore
    database=MYSQL_DATABASE,
)
cursor = connection.cursor()

cursor.execute(
    'CREATE TABLE IF NOT EXISTS users ('
    'id INT NOT NULL AUTO_INCREMENT, '
    'name VARCHAR(50) NOT NULL, '
    'age INT NOT NULL, '
    'PRIMARY KEY (id)'
    ')'
)

connection.commit()

cursor.close()
connection.close()
