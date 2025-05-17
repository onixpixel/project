import sqlite3

conn = sqlite3.connect('todo.db')

conn.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    completed INTEGER NOT NULL DEFAULT 0
)
''')

conn.commit()
conn.close()

print("Base de datos y tabla 'tasks' creadas o ya existían.")
