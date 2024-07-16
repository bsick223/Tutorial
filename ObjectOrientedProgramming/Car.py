class Car:


    # inside class outside constructor
    wheels = 4 #class variable

    # constructor
    def __init__(self, make, model, year, color):
        # assigning arguments to the attributes of car object.
        self.make = make      # instance variable
        self.model = model    # instance variable
        self.year = year      # instance variable
        self.color = color    # instance variable

    # method
    # self refers to the object using this method
    def drive(self):
        print(f"This {self.model} is driving")

    def stop(self):
        print(f"This {self.model} is stopped")
