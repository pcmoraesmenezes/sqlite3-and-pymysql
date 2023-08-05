import sqlite3
from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

# for row in cursor.fetchall():
#     value1, value2, value3 = row
#     print(value1, '\n', value2, '\n', value3, '\n')

cursor.execute(
    f'SELECT * FROM {TABLE_NAME} WHERE name="Paulo César"'
)
rows_to_delete = cursor.fetchall()

cursor.execute(
    f'DELETE FROM {TABLE_NAME} WHERE name="Paulo César"'
)
connection.commit()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

if __name__ == '__main__':
    print("DATA BASE BEFORE DELETION:")
    for row in cursor.fetchall():
        value1, value2, value3 = row
        print(value1, '\n', value2, '\n', value3, '\n')

# Fetch and store the data to be deleted
cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE name="Paulo César"')
rows_to_delete = cursor.fetchall()

# Delete the data
cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE name="Paulo César"')
connection.commit()


sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES'
    '(:nome, :peso)'  # Não precisa ser o mesmo nome
)

cursor.execute(
    sql,
    {
        'nome': 'Rafael',
        'peso': '67.63'
    },
)
connection.commit()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME} WHERE name="Rafael"'
)
if __name__ == '__main__':
    new_costumer = cursor.fetchall()
    print(f'DATA BASE AFTER ADDICTION OF {new_costumer}')

connection.commit()

cursor.close()
connection.close()
