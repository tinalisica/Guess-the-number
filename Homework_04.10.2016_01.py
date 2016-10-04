# Naredi igro Ugani skrito stevilo. V kodo hard-kodiraj neko stevilo. Uporabnik mora nato preko raw_input ugotoviti,
# katero je to stevilo. ce poda napacno stevilo, naj ga program na to opozori
#  (s print ukazom). ce pa skrito stevilo ugane, naj mu program cestita.


while True:
    x= raw_input("Guess the number from 1-9!")
    number = int(x)
    if number==5:
        print "Congratulations, the number we are looking for is 5!"
        break
    else:
        print "This is not the number we are looking for."





while True:
    x= raw_input ("Guess the number from 11-50!")
    number = int(x)
    if number==49:
        print "Yes, the number is 49!"
        break
    else:
        print "Wrong number, try again."




while True:
    x= raw_input ("Guess the number from 51-99!")
    number = int(x)
    if number==77:
        print "Yes, the number is 77!"
        break
    else:
        print "Wrong number, try again."