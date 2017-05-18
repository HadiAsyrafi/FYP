Python 2.7.12 (default, Nov 19 2016, 06:48:10) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> sql = '''
select *
from games
where rating like "E%"
'''
>>> result = cursor.execute(sql)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    result = cursor.execute(sql)
NameError: name 'cursor' is not defined
>>> import sqlite3
>>> conn = sqlite3.connect('games')
>>> conn = sqlite3.connect('mytest.db')
>>> cursor = conn.cursor()
>>> sql = ''' select *
from games
where rating like "E+"
'''
>>> results = cursor.execute(sql)
>>> all_e_games = results.fetchall()
>>> all_e_games
[]
>>> sql = ''' sfrom games
select *
where rating like "E+"
'''
>>> results = cursor.execute(sql)

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    results = cursor.execute(sql)
OperationalError: near "sfrom": syntax error
>>> sql = ''' from games
select *
where rating like "E+"
'''
>>> results = cursor.execute(sql)
>>> all_e_games = results.fetchall()
>>> all_e_games

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    results = cursor.execute(sql)
OperationalError: near "from": syntax error
>>> results = cursor.execute(sql)

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    results = cursor.execute(sql)
OperationalError: near "from": syntax error
>>> sql = '''from games
	select *
	where rating like "E%"'''
>>> e_games = cursor.execute(sql)

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    e_games = cursor.execute(sql)
OperationalError: near "from": syntax error
>>> sql = '''select *
	from games
	where rating like "E%"'''
>>> e_games = cursor.execute(sql)
>>> e_games = e_games.fetchall()
>>> e_games
[(u'Adventure Time', u'E10+', u'3DS', 2012), (u'Adventure Time', u'E10+', u'3DS', 2012), (u'Forza Motorsport 4', u'E', u'360', 2011), (u'Sonic Generations', u'E', u'3DS', 2012), (u'ZhuZhu Pets', u'E', u'Wii', 2012)]
>>> sql = ''' select *
from games
where rating like "E+"
'''
>>> results = cursor.execute(sql)
>>> all_e_games = results.fetchall()
>>> all_e_games
[]
>>>  sql = '''select *
	from games
	where rating like "E%"'''
 
  File "<pyshell#33>", line 1
    sql = '''select *
    ^
IndentationError: unexpected indent
>>>  sql = '''select *
from games
where rating like "E%"'''
 
  File "<pyshell#34>", line 1
    sql = '''select *
    ^
IndentationError: unexpected indent
>>> sql = '''select *
	from games
	where rating like "E%"'''
>>> results = cursor.execute(sql)
>>> all_e_games = results.fetchall()
>>> all_e_games
>>> results = cursor.execute(sql)
>>> 
>>> 
>>> all_e_games = results.fetchall()
>>> all_e_games
>>> 
>>> all_e_games
[(u'Adventure Time', u'E10+', u'3DS', 2012), (u'Adventure Time', u'E10+', u'3DS', 2012), (u'Forza Motorsport 4', u'E', u'360', 2011), (u'Sonic Generations', u'E', u'3DS', 2012), (u'ZhuZhu Pets', u'E', u'Wii', 2012)]
>>> sql = ''' select *
	from games
	where rating like "E%"'''
>>> results = cursor.execute(sql)
>>> all_e_games = results.fetchall()
>>> all_e_games
[(u'Adventure Time', u'E10+', u'3DS', 2012), (u'Adventure Time', u'E10+', u'3DS', 2012), (u'Forza Motorsport 4', u'E', u'360', 2011), (u'Sonic Generations', u'E', u'3DS', 2012), (u'ZhuZhu Pets', u'E', u'Wii', 2012)]
>>> sql = '''
select *
from games
where rating like "E%"
'''
>>> results = cursor.execute(sql)
>>> all_e_games = results.fetchall()
>>> all_e_games
[(u'Adventure Time', u'E10+', u'3DS', 2012), (u'Adventure Time', u'E10+', u'3DS', 2012), (u'Forza Motorsport 4', u'E', u'360', 2011), (u'Sonic Generations', u'E', u'3DS', 2012), (u'ZhuZhu Pets', u'E', u'Wii', 2012)]
>>> sql = ''' select *
from games
where rating like "E+"
'''
>>> results = cursor.execute(sql)
>>> all_e_games = results.fetchall()
>>> all_e_games
>>> sql = ''' select *
from games
where rating like "E+"
'''
>>> esults = cursor.execute(sql)
>>> results = cursor.execute(sql)
>>> all_e_games = results.fetchall()
>>> all_e_games
[]
>>> sql = ''' select *
from games
where rating like "E+%"
'''
>>> results = cursor.execute(sql)
>>> all_e_games = results.fetchall()
>>> all_e_games
[]
>>> sql = ''' select *
from games
where rating like "E%"
'''
>>> results = cursor.execute(sql)
>>> all_e_games = results.fetchall()
>>> all_e_games
[(u'Adventure Time', u'E10+', u'3DS', 2012), (u'Adventure Time', u'E10+', u'3DS', 2012), (u'Forza Motorsport 4', u'E', u'360', 2011), (u'Sonic Generations', u'E', u'3DS', 2012), (u'ZhuZhu Pets', u'E', u'Wii', 2012)]
>>> sql = ''' select *
from games
where rating like "E%"
'''
>>> sql = ''' select *
from games
where rating like "%E%"
'''
>>> all_e_games = results.fetchall()
>>> all_e_games
[]
>>> sql = ''' select *
from games
where rating like "E%"
'''
>>> sql = ''' select *
from games
where rating like "%E%"
'''
>>> results = cursor.execute(sql)
>>> all_e_games = results.fetchall()
>>> all_e_games
[(u'Adventure Time', u'E10+', u'3DS', 2012), (u'Adventure Time', u'E10+', u'3DS', 2012), (u'Forza Motorsport 4', u'E', u'360', 2011), (u'Sonic Generations', u'E', u'3DS', 2012), (u'ZhuZhu Pets', u'E', u'Wii', 2012)]
>>> sql = ''' select *
from games
where rating not like "%E%"
'''
>>> results = cursor.execute(sql)
>>> all_e_games = results.fetchall()
>>> all_e_games
[(u'Tales of the Abyss', u'T', u'3DS', 2011), (u'T', u'3DS', u'2011', u'sdf'), (u'af', u'adf', u'adf', u'adf'), (u'Tales of the Abyss', u'T', u'3DS', 2011), (u'Hollywood Crimes', u'T', u'3DS', 2011), (u'Forza Horizon', u'T', u'360', 2012)]
>>> sql = ''' select *
from games
where year > 2011
'''
>>> results = cursor.execute(sql)
>>> all_e_games = results.fetchall()
>>> all_e_games
[(u'Adventure Time', u'E10+', u'3DS', 2012), (u'T', u'3DS', u'2011', u'sdf'), (u'af', u'adf', u'adf', u'adf'), (u'Adventure Time', u'E10+', u'3DS', 2012), (u'Sonic Generations', u'E', u'3DS', 2012), (u'Forza Horizon', u'T', u'360', 2012), (u'ZhuZhu Pets', u'E', u'Wii', 2012)]
>>> sql = ''' select title
from games
order by title
'''
>>> results = cursor.execute(sql)
>>> all_e_games = results.fetchall()
>>> all_e_games
[(u'Adventure Time',), (u'Adventure Time',), (u'Forza Horizon',), (u'Forza Motorsport 4',), (u'Hollywood Crimes',), (u'Sonic Generations',), (u'T',), (u'Tales of the Abyss',), (u'Tales of the Abyss',), (u'ZhuZhu Pets',), (u'af',)]
>>> ql = ''' select title
from games
order by title desc
'''
>>> results = cursor.execute(sql)
>>> all_e_games = results.fetchall()
>>> all_e_games
[(u'Adventure Time',), (u'Adventure Time',), (u'Forza Horizon',), (u'Forza Motorsport 4',), (u'Hollywood Crimes',), (u'Sonic Generations',), (u'T',), (u'Tales of the Abyss',), (u'Tales of the Abyss',), (u'ZhuZhu Pets',), (u'af',)]
>>> sql = ''' select title
from games
order by title desc
'''
>>> results = cursor.execute(sql)
>>> all_e_games = results.fetchall()
>>> all_e_games
[(u'af',), (u'ZhuZhu Pets',), (u'Tales of the Abyss',), (u'Tales of the Abyss',), (u'T',), (u'Sonic Generations',), (u'Hollywood Crimes',), (u'Forza Motorsport 4',), (u'Forza Horizon',), (u'Adventure Time',), (u'Adventure Time',)]
>>> sql = '''
select distinct system
from games
'''
>>> results = cursor.execute(sql)
>>> systems = results.fetchall()
>>> systems
[(u'3DS',), (u'2011',), (u'adf',), (u'360',), (u'Wii',)]
>>> sql = '''
update games
set title="Adventure Time"
where title="Adventureres Lake"
'''
>>> results = cursor.execute(sql)
>>> systems = results.fetchall()
>>> systems
[]
>>> conn.commit()
>>> sql = ''' select title
from games
order by title
'''
>>> results = cursor.execute(sql)
>>> systems = results.fetchall()
>>> systems
[(u'Adventure Time',), (u'Adventure Time',), (u'Forza Horizon',), (u'Forza Motorsport 4',), (u'Hollywood Crimes',), (u'Sonic Generations',), (u'T',), (u'Tales of the Abyss',), (u'Tales of the Abyss',), (u'ZhuZhu Pets',), (u'af',)]
>>> sql = '''
update games
set title="Adventures Lake"
where title="Adventurere Time"
'''
>>> conn.commit()
>>> sql = ''' select title
from games
order by title
'''
>>> results = cursor.execute(sql)
>>> systems = results.fetchall()
>>> systems
[(u'Adventure Time',), (u'Adventure Time',), (u'Forza Horizon',), (u'Forza Motorsport 4',), (u'Hollywood Crimes',), (u'Sonic Generations',), (u'T',), (u'Tales of the Abyss',), (u'Tales of the Abyss',), (u'ZhuZhu Pets',), (u'af',)]
>>> sql = '''
update games
set title="Adventures Lake"
where title="Adventure Time"
'''
>>> cursor.execute(sql)
<sqlite3.Cursor object at 0x7ff9f003e7a0>
>>> conn.commit()
>>> sql = ''' select title
from games
order by title
'''
>>> results = cursor.execute(sql)
>>> systems = results.fetchall()
>>> systems
[(u'Adventures Lake',), (u'Adventures Lake',), (u'Forza Horizon',), (u'Forza Motorsport 4',), (u'Hollywood Crimes',), (u'Sonic Generations',), (u'T',), (u'Tales of the Abyss',), (u'Tales of the Abyss',), (u'ZhuZhu Pets',), (u'af',)]
>>> cursor.execute("delete from games where title=\"Adventures Lake"")
	       
SyntaxError: EOL while scanning string literal
>>> cursor.execute("delete from games where title=\"Adventures Lake\"")
<sqlite3.Cursor object at 0x7ff9f003e7a0>
>>> conn.commit()
>>> sql = ''' select title
from games
order by title
'''
>>> results = cursor.execute(sql)
>>> systems = results.fetchall()
>>> systems
[(u'Forza Horizon',), (u'Forza Motorsport 4',), (u'Hollywood Crimes',), (u'Sonic Generations',), (u'T',), (u'Tales of the Abyss',), (u'Tales of the Abyss',), (u'ZhuZhu Pets',), (u'af',)]
>>> 
