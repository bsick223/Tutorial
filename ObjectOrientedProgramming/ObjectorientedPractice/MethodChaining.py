# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("You Start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self

car = Car()
# after first method, python must return self or car for car.drive
#car.turn_on().drive()

# car.turn_on()
# car.drive()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
