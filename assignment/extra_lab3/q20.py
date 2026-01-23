# method overriding
class car:
    def colur(self):
        print("colour of this car is blue")

class bike(car):
    def colur(self):
        print("clour  of this bike is black")

b1=bike()
b1.colur()