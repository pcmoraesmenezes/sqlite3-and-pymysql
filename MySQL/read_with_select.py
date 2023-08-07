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

cursor.execute(f'SELECT * FROM {TABLE_NAME}')  # O asterisco indica que irá
#  Selecionar tudo
for row in cursor.fetchall():
    print(row)


print()

cursor.execute(f'SELECT name FROM {TABLE_NAME}')  # Ou pode-se passar o(s)
# Campo(s) desejados
for row in cursor.fetchall():
    # if "Paulo" in row:
    #     print('ok')
    print(row)

print()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')
one_by_one = cursor.fetchone()
print(one_by_one)

print()

cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE name = %s', ("Medina",))
result = cursor.fetchone()

if result:
    print(result)
else:
    print('Name not found')

print()

num_rows_to_retrieve = 5  # Número de linhas a serem recuperadas
cursor.execute(f'SELECT * FROM {TABLE_NAME} LIMIT %s', (num_rows_to_retrieve,))

result = cursor.fetchall()

for row in result:
    print(row)

cursor.execute(
    f'SELECT '
    f'(SELECT name FROM {TABLE_NAME} WHERE id = %s) AS vitor_ruba_name, '
    f'(SELECT age FROM {TABLE_NAME} WHERE name = %s) AS rickson_jovem_age, '
    f'(SELECT id FROM {TABLE_NAME} WHERE name = %s) AS joao_paulo_id '
    f'FROM {TABLE_NAME} '
    f'WHERE name = %s',
    (4, "Rickson Jovem", "João Paulo", "Vitor Ruba")
)
print()

result = cursor.fetchone()
if result:
    print('NAME ID 4 :', result[0])
    print('AGE OF RICKSON_JOVEM:', result[1])
    print('ID OF JOÃO PAULO:', result[2])
cursor.close()
connection.close()
