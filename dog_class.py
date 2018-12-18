class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

# Access the instance attributes
print("{} is {} and {} is {}.".format(
    philo.name, philo.age, mikey.name, mikey.age))

# Is Philo a mammal?
if philo.species == "mammal":
    print("{0} is a {1}!".format(philo.name, philo.species))

# Review Exercise 1
#Using the same Dog class, instantiate three new dogs, each with a different age. Then write a function called, get_biggest_number(), that takes any number of ages (*args) and returns the oldest one. Then output the age of the oldest dog like so:

#The oldest dog is 7 years old.
alpha = Dog("Alpha", 10)
beta = Dog("Beta", 9)
gamma = Dog("Gamma", 8)

def get_biggest_number(*args):
    return max(args)

print("The oldest dog is {} years old.").format(get_biggest_number(alpha.age, beta.age, gamma.age))
