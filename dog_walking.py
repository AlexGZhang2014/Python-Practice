# Create a Pets class that holds instances of dogs; this class is completely separate from the Dog class. In other words, the Dog class does not inherit from the Pets class. Then assign three dog instances to an instance of the Pets class. Start with the following code below. Save the file as pets_class.py. Your output should look like this:

# I have 3 dogs.
# Tom is 6.
# Fletcher is 7.
# Larry is 9.
# And they're all mammals, of course.
# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    # Instance method
    def eat(self):
        self.is_hungry = False

    # Instance method
    def walk(self):
        return "{} is walking!".format(self.name)

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)

class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())

# Create instances of dogs
my_dogs = [
    Bulldog("Tom", 6),
    RussellTerrier("Fletcher", 7),
    Dog("Larry", 9)
]

# Instantiate the Pets class
my_pets = Pets(my_dogs)

# Output
my_pets.walk()
