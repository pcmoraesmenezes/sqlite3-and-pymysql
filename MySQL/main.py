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
cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')

connection.commit()

sql = (
       f'INSERT INTO {TABLE_NAME} '
       '(name, age) '
       'VALUES '
       '(%s, %s)'
    )

name = input('Please enter the name: ')
age = input('Now enter the age: ')
data = (name, age)

cursor.execute(sql, data)

cursor.execute(sql, ('Antonio Brazino', 22))

data_with_dict = {
    "name": "Rickson Jovem",
    "age": 31923,
}

sql_with_dict = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, age) '
    'VALUES '
    '(%(name)s, %(age)s)'
)

cursor.execute(sql_with_dict, data_with_dict)
connection.commit()

many_data = [
    {"name": "Vitor Ruba", "age": 23},
    {"name": "João Paulo", "age": 27},
    {"name": "Ygor", "age": 22},
]

sql_many = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, age) '
    'VALUES '
    '(%(name)s, %(age)s)'
)

cursor.executemany(sql_many, many_data)

tuple_of_tuple = [
    ("Brancudo - White ", 21),
    ("Felipe - Dylon", 20),
    ("Rafael Fort", 20),
]

cursor.executemany(sql, tuple_of_tuple)

cursor.executemany(sql_many,
                   [
                       {"name": "Medina", "age": 20},
                       {"name": "Vinicius", "age": 20},
                       {"name": "Samuca", "age": 22},
                   ])

connection.commit()

cursor.execute(f'SELECT id, name, age FROM {TABLE_NAME}')
results = cursor.fetchall()
for row in results:
    id = row[0]
    name = row[1]
    age = row[2]
    print(f"ID: {id}, Name: {name}, Age: {age}")

cursor.close()
connection.close()
