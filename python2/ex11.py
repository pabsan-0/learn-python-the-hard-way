print "How old are you?",
age = input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()


# raw input doesnt crash if input is void

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

print "So, you're %s old, %s tall and %s heavy." % (
    age, height, weight)


# multiplies input by 2 (number)
print age * 2

# prints twice the input (raw/str)
print height * 2

# thats how its done
print int(height) * 2




# every input crashes if using symbols as ' "
#print "How old are you?",
#age = input()
#print "How talla are you?",
#height = input()
#print "How much do you weigh?",
#weight = input()

#print "So, you're %r old, %r tall and %r heavy." % (
#    age, height, weight)

#print "So, you're %s old, %s tall and %s heavy." % (
#    age, height, weight)
