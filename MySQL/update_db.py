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

sql = (
    f'UPDATE {TABLE_NAME} '
    f'SET name=%s, age=%s '
    f'WHERE id=%s'
)
cursor.execute(sql, ('Roosevelt', 21, 6))
connection.commit()
