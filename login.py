import datetime
import os
import time

popitka = 0
citata1 = "fghfdgghdgafdgdg gdgadf gdfg etrtertdf g"
citata2 = "hdhstgdf dfh sh shsdf hsh s h serterthsh sf h"
citata3 = "gfhsfhg fshgsffhj sf fghsf hsh retertertth"

while popitka <=3:
	print ("vvedite vash login"),
	login=raw_input(">>>")
	print ("vvedite vash parol"),
	parol=raw_input(">>>")
	if (login == "admin") and (parol == "12345"):

		new_date = datetime.date.today()
		print new_date
		year = new_date.year
		print os.name
		break
	else:
		print "vy vveli nevernyi login ili parol"
		popitka +=1
		time.sleep (5)
		citata=randint(1,3)

		if citata == 1:
			print citata1
		elif citata==2:
			print citata2
		else:
			print citata3
		print "vashi popytki zakonchilis'" 