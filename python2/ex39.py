# Dicts / hashes
#   dict.items() -> returns a list of elements in a tuple
#   a = dict.get('Texas', None) -> check if it can find it. wont break if it isnt there
#       In case of failure, the command to the right is run (None)
#       If assigning to a variable, the command output goes to the variable

#----------------------------------------------------
# quick example on how to call a func from a dir
def funny():
    print "hello"
mestuff = {'apple': "I AM APLES!",
           'stringed': funny}
mestuff['stringed']()

# or

def funny():
    print "hello"
mestuff = {'apple': "I AM APLES!",
           'stringed': funny()}
mestuff['stringed']() # <-- necesario
#----------------------------------------------------

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city fot the state 'TX' is: %s" % city

print '-' * 20
print states.items()        # lista
print '-' * 10
print states.iteritems()    # generador
