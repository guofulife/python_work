filename = 'guest_book.txt'
with open(filename, 'a') as file_object:
	guest=""
	while guest!=' ':
		guest=input('\nTell me What is your name:')
		file_object.write('\n'+guest)
