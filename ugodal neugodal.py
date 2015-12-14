from random import randint
print "Tebe nado ugadat' chislo, cotoroe ya zagadau"
print "vvedi predel chisel" 
m = int(raw_input(">>>"))
x = randint(0,m)
logic=0
popitka=3
while (logic !=1):
	
	print "vvedite chislo"
	log = int(raw_input(">>>"))
	if x == log:
 		print "ty ugodal"
 		logic=1
 	else:
		print "ty ne ugodal, jalkii smertnyi"
		print "poprobui snova"
	popitka +=1
	print