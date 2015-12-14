for n in xrange(1, 10):
    if n % 15 == 0:
        print "FizzBuzz"
    elif n % 3 == 0:
        print "Fizz"
    elif n % 5 == 0:
        print "Buzz"
    else:
        print n