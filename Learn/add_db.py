import sqlite3

conn = sqlite3.connect('mytest.db')
cursor = conn.cursor()
print "Let's input some students!"
while True:
	name = raw_input('Students\'s name: ')
	username = raw_input('Student\'s username: ')
	id_num = raw_input('Students\'s id number: ')
	sql = ''' insert into students
		(name, username, id)
		values
		(:st_name, :st_username, :id_num)'''

	cursor.execute(sql, {'st_name':name, 'st_username':username, 'id_num':id_num})
	conn.commit()
	cont = raw_input("Another student? ")
	if cont[0].lower() == 'n':
		break
cursor.close()
