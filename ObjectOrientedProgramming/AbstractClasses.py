"""
Prevents a user from creating an object of that class (Ghost class)
+ compels a user to override abstract methods in a child class

abstract class = a class which contains one or more abstract methods.
abstract method = a method that has a declaration but does not have an implementation

benefits, prevents the user from creating an object of that class
compels user to override any methods in a child class

"""
 # abc = abstract base class
from abc import ABC, abstractmethod

class Vehile(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehile):

    # we must ovveride the abstract class
    def go(self):
        print("you drive the car")

    def stop(self):
        print("This car has stopped")


class Motorcycle(Vehile):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcyle has stopped")


vehicle = Vehile()
car = Car()
motorcycle = Motorcycle()

vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()
