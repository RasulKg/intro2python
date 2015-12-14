print "vvedite new parol"
s = raw_input (">>>")
for char in s:
	if char == 'q':
		char = 'r'
	elif char == 'r':
		char = 's'
	elif char == 's':
		char = 't'
	elif char == 't':
		char = 'v'
	elif char == 'v':
		char = 'x'
	elif char == 'x':
		char = 'y'
	elif char == 'y':
		char = 'z'
	elif char =='z':
		char = '@'
	print char