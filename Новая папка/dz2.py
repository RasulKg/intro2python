print "vvedi parol"
s = raw_input (">>>")
for char in s:
	if char == 'r':
		char = 'q'
	elif char == 's':
		char = 'r'
	elif char == 't':
		char = 's'
	elif char == 'v':
		char = 't'
	elif char == 'x':
		char = 'v'
	elif char == 'y':
		char = 'x'
	elif char == 'z':
		char = 'y'
	elif char =='@':
		char = 'z'
	print char