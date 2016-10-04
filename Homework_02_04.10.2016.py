stevec = 0
while stevec <= 2:

    x= raw_input("Guess a number from 1-33!")
    number = int(x)
    if number==9:
        print "Yes, 9 is the number we are looking for!"
        break
    if number!=9:
        print "Sorry, the number is not %s." %number
        print "Number of remaining tries: %s" % (2-stevec)
        stevec = stevec+1


