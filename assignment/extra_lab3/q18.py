class car:
    def __init__(self):
        print("this is a class car")

class bike(car):
    def __init__(self):
       super().__init__()
       print("this  is a class bike")

b1=bike()


