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

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
    'id INT NOT NULL AUTO_INCREMENT, '
    'name VARCHAR(50) NOT NULL, '
    'age BIGINT NOT NULL, '
    'PRIMARY KEY (id)'
    ')'
)
cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')  # Isso limpa a tabela

connection.commit()

sql = (
       f'INSERT INTO {TABLE_NAME} '
       '(name, age) '
       'VALUES '
       '(%s, %s) '
    )

name = input('Please info the name: ')
age = input('Now the age: ')
data = (name, age)

cursor.execute(sql, (data))

cursor.execute(
    # f'INSERT INTO {TABLE_NAME} '
    # '(name, age) VALUES ("Paulo", 19) '
    sql, ('Antonio Brazino', 22)  # PARA EVITAR SQL INJECTION
)
connection.commit()

data_with_dict = {
    "this_variable_name_dont_import": "Rickson Jovem",
    "that_too": 31923,
}

sql_with_dict = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, age) '
    'VALUES '
    '(%(this_variable_name_dont_import)s, %(that_too)s) '
)

cursor.execute(sql_with_dict, data_with_dict)
connection.commit()

cursor.close()
connection.close()
