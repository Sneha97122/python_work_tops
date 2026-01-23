class car:
    def colur(self):
        print("this car color is blue")

class truck(car):
    def pattern(self):
        print("this is a truck pattern")

class bike(truck):
    def design(self):
        print("this bike design is black")

b1=bike()
b1.colur()
b1.design()
b1.pattern()