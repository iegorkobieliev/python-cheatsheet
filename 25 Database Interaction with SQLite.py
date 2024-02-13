# import sqlite3
#
# conn = sqlite3.connect('example.db')
# cursor = conn.cursor()
#
# # Execute SQL query
# cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
#
# # Commit changes
# conn.commit()
#
# # Close connection
# conn.close()


# 41 Database Interaction with SQLite

import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('mydatabase.db')
cursor1 = conn.cursor()
cursor1.execute('CREATE TABLE IF NOT EXISTS mytable (id INTEGER PRIMARY KEY, name TEXT)')
conn.commit()

cursor2 = conn.cursor()

# Execute SQL query
result = cursor2.execute('SELECT * FROM mytable')
# print(cursor)
print(result)
print(type(result))
print(list(result))
