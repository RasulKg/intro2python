import datetime
now_date=datetimedate. today
year= now_date. year
month=now_date. month
day=now_date. day
print year,"-",month,"-",day
print "vvedite god rojdenya"
byear= raw_input (">")
print "vvedite mesyac rojdenya"
bmonth=raw_input (">")
print "vvedite den' rojdenya"
bday=raw_input(">")
print (int(year)-int(byear)*365+(int(month)-int(bmonth))30.5) +int(bday))