import sqlite3

conn = sqlite3.connect('mytest.db')
cursor = conn.cursor()
print "Let's input some games informations!"
while True:
	title = raw_input('Games\'s title: ')
	rating = raw_input('Games\'s rating: ')
	system = raw_input('Games\'s system: ')
	year = raw_input('Games\'s year of release: ')
	sql = ''' insert into games
		(title, rating, system, year)
		values
		(:game_title, :game_rating, :game_system, :game_year)'''

	cursor.execute(sql, {'game_title':title, 'game_rating':rating, 'game_system':system,
			'game_year':year})
	conn.commit()
	cont = raw_input("Another game? ")
	if cont[0].lower() == 'n':
		break
cursor.close()
