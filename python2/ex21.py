def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def substract(a, b):
    print "SUBSTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "lets do some math"

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)


print "Age: %d, height: %d, weight %d, iq: %d" % (age, height, weight, iq)

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print "that becomes:", what, "Can you do it by hand?"
print "that becomes:"+ str(what), "Can you do it by hand?" # + can only concatenate str
