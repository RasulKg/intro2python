import datetime
import os
from random import randint

now_date = datetime.date.today()


login = "admin"
password = 12345
popitka = 0
pop = 3

fst = "Leadership is a choice you make,\nnot a place you sit.\n\t\t\t-John C.Maxwell"
sec = "All the beautiful sentiments in the world\nweight less than a single lovely action.\n\t\t\t-James Russell Lowel"
thir = "Do something you hate every day,\njust for practice.\n\t\t\t-John C.Maxwell"
four = "I'm a great believer in luck,\nand i find that the harder i work,\nthe more i have of it."


while popitka < pop:
	
	print "Vvedite login"
	l = raw_input(">")
 
	print "Vvedite parol"
	p = int(raw_input(">"))

	if l == login and p == password:
		print now_date, os.name
		break
	else:
		print "Ne vernii login ili parol\nPovtorite popitky"
	x = randint(1,4)
	if x == 1:
		print fst
	elif x == 2:
		print sec
	elif x == 3:
		print thir
	elif x == 4:
		print four
	popitka += 1

	import time
	time.sleep(5)
print "Y vas zakon4ilis popitki"		
