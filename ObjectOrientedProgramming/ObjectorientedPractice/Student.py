class Student:

    def __init__(self, name, gender, GPA, age):
        self.name = name
        self.gender = gender
        self.GPA = GPA
        self.age = age

    def study(self):
        print(f"{self.name} is studying")
    def chill(self):
        print(f"{self.name} is chilling")
