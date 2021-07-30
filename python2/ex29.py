from sys import argv

script, ppl = argv

# print people
# print people

people = int(ppl) # weird behaviour when comparing int and str in python2 
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! the world is doomed!"

if people > cats:
    print "Not many cats! the world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"


dogs += 5

if people >= dogs:
    print "people are greater than or equal to dogs"

if people <= dogs:
    print "people are less than or equal to dogs"

if people == dogs:
    print "people are dogs"
