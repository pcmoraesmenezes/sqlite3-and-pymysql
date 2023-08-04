import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Cuidado delete sem WHERE
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'  # Apaga TODOS os valores da tabela
)
connection.commit()

#  Limpar os IDS
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT, '
    'weight REAL'
    ')'
)
connection.commit()

# Registrar valores nas colunas da tabela
# sql = (
#     f'INSERT INTO {TABLE_NAME} '
#     ' (id, name, weight)'
#     ' VALUES'
#     '(NULL, "Paulo César", 20.35),'
#     '(NULL, "Antonio", 29.47)',
# )  # Executa um comando sql

# sql = (
#     f'INSERT INTO {TABLE_NAME} '
#     '(name, weight) '
#     'VALUES'
#     '(?, ?)'
# )

sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES'
    '(:nome, :peso)'  # Não precisa ser o mesmo nome
)


# cursor.execute(sql, ['Rickson', 53.79])
# cursor.executemany(sql, Execute many sempre será uma lista
#                    [
#                        ['Rickson', 73.976],
#                        ['Antonio Brazino', 68.97],
#                        ['Paulo César', 66.73]
#                     ]
#                    )

# cursor.execute(
#     sql, {
#         'nome': 'Paulo',
#         'peso': 68.93
#     }
#                )

cursor.executemany(
    sql,
    [
        {
            'nome': 'Paulo César',
            'peso': 63.89
        },

        {
            'nome': 'Antonio Brazino',
            'peso': 68.94
        },

        {
            'nome': 'Rickson',
            'peso': 77.94
        }
    ]
)

connection.commit()
# cursor.executemany  # Executa varios comandos


cursor.close()
connection.close()
