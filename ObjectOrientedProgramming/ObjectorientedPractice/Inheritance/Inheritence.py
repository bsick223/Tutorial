class Animal:
    # parent class

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


# Child class - inherit everything from parent/common class
# Similar to having a global variable
class Rabbit(Animal):

    def run(self):
        print("this rabbit is running!")


class Fish(Animal):

    def swim(self):
        print("This fish is swimming")


class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

#print(rabbit.alive)
#fish.eat()
#hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()
