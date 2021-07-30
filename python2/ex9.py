# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"

# \n === line break
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print "here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

print "here are the days: %s " % days
print "Here are the months: %s" % months
# print "Here are the months: %d" % months; D requires numbers!

print "Here are the months: %r" % months
