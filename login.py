import datetime
print ("vvedite vash login")
login=raw_input(":")
print ("vvedite vash parol")
parol=raw_input(":")
if (login == "admin") and (parol == "12345"):

	new_date = datetime.date.today()
	print new_date
	year = new_date.year
	print 
else:
	print ("nevernyi login ili parol")


