def mientras(lim, inc):
    numbers = []
    i = 0
    while i < lim:
        print "At the top i helis %d" % i
        numbers.append(i)

        i = i + inc
        print "Numbers now: ", numbers
        # print "Numbers now: %s" % numbers

        print "At the bottom is %d" % i

    print "The numbers: "

    for num in numbers:
        print num


# Modifying the value of the iterating variable in python might not break the program
# In python, the variable is grabbed from an iterable at each iteration, not updated

def forro(lim, inc):
    numbers = []
    i = 0
    for i in range(lim):
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + inc
        print "Numbers now: ", numbers
        # print "Numbers now: %s" % numbers

        print "At the bottom is %d" % i

    print "The numbers: "

    for num in numbers:
        print num


# It does have an impact now because i modified then used it.
def forro2(lim, inc):
    numbers = []
    i = 0
    for i in range(lim):
        print "At the top i is %d" % i
        i = i + inc               
        numbers.append(i)


        print "Numbers now: ", numbers
        # print "Numbers now: %s" % numbers

        print "At the bottom is %d" % i

    print "The numbers: "

    for num in numbers:
        print num
