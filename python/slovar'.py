D = {'cat':'koshka','dog':'sobaka','snake':'zmeya'}
print D
print "Dlya prosmotra slovorya najmite 1"
print "Dlya dobavleniya najmite 2"
choise = raw_input (">>>")
add = "1"
if choise == "1":
	for key in D:
		print key,"-",D[key]
elif choise == "2":
	while add == "1":
		print "Vvedite slovo na english yazyke"
		dkey = raw_input (">>>")
		print "Vvedite perevod"
		dval = raw_input (">>>")
		print D 
		print "dlya dobavleniya esho odnogo slova najmite 1"
		print "dlya prosmotra slovorya najmite 2"
		print "dlya vyhoda najmite lubuy klavishu"
		add = raw_input (">>>")
		D[dkey] = dval
		for key in D:
			print key,"-",D[key]	
else:
	print "Dlya prosmotra slovorya najmite 1"
	print "Dlya dobavleniya najmite 2"
	choise = raw_input (">>>")
	