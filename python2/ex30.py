# multiple elifs in same conditional -> only the first true one is run


people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take the cars"
elif cars < people:
    print "we should not take the cars."
else: 
    print "we cant decide"
    
if buses > cars:
    print "That's too many buses"
elif buses < cars:
    print "maybe we could take the buses"
else: 
    print "we still can't decide"
    
if people > buses:
    print "alright, lets just take the buses"
else:
    print "Fine, let's stay home then."
    
    
    