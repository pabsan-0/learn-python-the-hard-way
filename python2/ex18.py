# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args  is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg: %r" % arg1

def print_none():
    print "i got nothin'"

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()