import sqlite3

conn = sqlite3.connect('mytest.db')
cursor = conn.cursor()
sql = '''create table games(
	title text,
	rating text,
	system text,
	year int)'''
cursor.execute(sql)
cursor.close()

