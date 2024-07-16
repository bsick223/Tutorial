# multi-level inheritance = when a derived (child) class inherits another derived (child) class

# Grand - Parent
class Organism:

    alive = True

# parent
class Animal(Organism):

    def eat(self):
        print("This animal is eating")

# child
class Dog(Animal):

    def bark(self):
        print("this dog is barking")

dog = Dog()

print(dog.alive)
dog.eat()
dog.bark()
