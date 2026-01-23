class car:
    def colur(self):
        print("this car colour is red")

class bike(car):
    pass
   

class truck(car):
    pass


b1=bike()
t1=truck()
b1.colur()
t1.colur()