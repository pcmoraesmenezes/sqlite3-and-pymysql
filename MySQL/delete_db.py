import pymysql
from dotenv import load_dotenv
import os


load_dotenv()

MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_HOST = os.getenv('MYSQL_HOST')
TABLE_NAME = 'users'

connection = pymysql.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,  # type: ignore
    database=MYSQL_DATABASE,
)
cursor = connection.cursor()

os.system('cls' if os.name == 'nt' else 'clear')

cursor.execute(
    f'SELECT name, age FROM {TABLE_NAME}'
)


sql = (
     f'DELETE FROM {TABLE_NAME} '
     'WHERE age = %s'
)

cursor.execute(sql, (20))
connection.commit()

print('\n', '-' * 50, 'DATA BASE AFTER DELETE AGES = 20', '-' * 50, '\n')

cursor.execute(
    f'SELECT name, age FROM {TABLE_NAME}'
)

for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()
