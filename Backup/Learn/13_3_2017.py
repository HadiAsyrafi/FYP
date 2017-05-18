Python 2.7.12 (default, Nov 19 2016, 06:48:10) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import sqlite3
>>> conn == sqlite3.connect('mytest.db')

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    conn == sqlite3.connect('mytest.db')
NameError: name 'conn' is not defined
>>> conn = sqlite3.connect('mytest.db')
>>> cursor = conn.cursor()
>>> sql = '''FROM games
	SELECT *
	WHERE rating="E"'''
>>> e_games = cursor.execute(sql)

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    e_games = cursor.execute(sql)
OperationalError: near "FROM": syntax error
>>> sql = '''from games
	select *
	where rating="E"'''
>>> e_games = cursor.execute(sql)

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    e_games = cursor.execute(sql)
OperationalError: near "from": syntax error
>>> sql = '''select *
	from games
	where rating="E"'''
>>> e_games = cursor.execute(sql)
>>> e_games = e_games.fetchall()
>>> e_games
[(u'Forza Motorsport 4', u'E', u'360', 2011), (u'Sonic Generations', u'E', u'3DS', 2012), (u'ZhuZhu Pets', u'E', u'Wii', 2012)]
>>> sql = '''SELECT *
	from games
	where rating="E"'''
>>> result = cursor.execute(sql)
>>> e_games = result.fetchall()
>>> e_games
[(u'Forza Motorsport 4', u'E', u'360', 2011), (u'Sonic Generations', u'E', u'3DS', 2012), (u'ZhuZhu Pets', u'E', u'Wii', 2012)]
>>> sql = '''select *
	from games
	where rating!="E"'''
>>> result = cursor.execute(sql)
>>> not_e_games = result.fetchall()
>>> not_e_games
[(u'Tales of the Abyss', u'T', u'3DS', 2011), (u'Adventure Time', u'E10+', u'3DS', 2012), (u'T', u'3DS', u'2011', u'sdf'), (u'af', u'adf', u'adf', u'adf'), (u'Tales of the Abyss', u'T', u'3DS', 2011), (u'Adventure Time', u'E10+', u'3DS', 2012), (u'Hollywood Crimes', u'T', u'3DS', 2011), (u'Forza Horizon', u'T', u'360', 2012)]
>>> 
