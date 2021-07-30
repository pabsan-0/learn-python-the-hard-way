def cheese_and_crackers(cheese_count = 0, boxes_of_crackers = 2):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "man thats enough for a party"
    print "Get a blanket. \n"
    
    
print "we can just give the function numbers directly"
cheese_and_crackers(20, 30)

print "or we can use variables for our scripts"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "we can even do math inside"
cheese_and_crackers(10 + 20, 5 + 6)

print "and we can combine the two, variables and math"
cheese_and_crackers(amount_of_cheese + 20, amount_of_crackers + 6)

# cheese_and_crackers(,2)  # error
# cheese_and_crackers()    # defaults