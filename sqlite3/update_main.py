import sqlite3
from main import DB_FILE, TABLE_NAME


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)

for row in cursor.fetchall():
    _id, name, weight = row
    print(f'id: {_id}, name: {name}, weight: {weight}')
    print()

cursor.execute(
    f'UPDATE {TABLE_NAME} '
    'SET name="Vitor Rubatino", weight="163.74" '
    'WHERE name="Paulo César"'
)
connection.commit()

print('DATA BASE AFTER CHANGES: ')
print()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)
for row in cursor.fetchall():
    _id, name, weight = row
    print(f'id: {_id}, name: {name}, weight: {weight}')
    print()

cursor.close()
connection.close()
