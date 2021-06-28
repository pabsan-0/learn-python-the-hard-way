## Animal is-a object
class Animal(object):
    pass

# ?? dog is an animal
class Dog(Animal):
    def __init__(self, name):
        # ?? dog has a name
        self.name = name

## ?? cat is an animal
class Cat(Animal):
    def __init__(self, name):
        ## ?? cat has a name
        self.name = name

# ?? person is an object
class Person(object):
    def __init__(self, name):
        ## ?? person has a name
        self.name = name
        # Person has-a pet of some kind
        self.pet = None

## ?? employee is a person
class Employee(Person):
    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??  employee has a salary
        self.salary = salary

## ?? fish is an object
class Fish(object):
    pass

## ?? salmon is a fish
class Salmon(Fish):
    pass

## ?? halibut is a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog('Rover')

## ?? satan is a cat
satan = Cat('Satan')

## ?? mary is a person
mary = Person('Mary')

## ??  mary has a pet
mary.pet = satan

## ?? frank is an employee
frank = Employee('Frank', 120000)

## ?? frank has a pet, frank.pet is a Dog, frank.pet has a name which is Rover
frank.pet = rover

## ?? flipper is a fish
flipper = Fish()

# ?? crouse is a salmon
crouse = Salmon()

# ?? harry is a halibut
harry = Halibut()


#### additional

class Pablo(Person):
    def __init__(self, name):
        pass

pablo = Pablo('pablo')

# This breaks
# print(pablo.name}

class Pablo2(Person):
    def __init__(self, name):
        super(Pablo2, self).__init__(name)

pablo2 = Pablo2('pablo2')
print(f'This does not break {pablo2.name}')



