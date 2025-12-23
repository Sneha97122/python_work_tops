# class pen:
#     price =10
#     color="red"

#     def __init__(self,id,name):
#         self.id= id
#         self.name = name
#         print("this is constructor")
    
#     def to_write(self):
#         print("witing somthing..")
#         print(self.price,self.color)

#     def display(self):
#         print(self.id,self.name)

# p1 =pen(10,"abc")
# p1.to_write()
# p1.display()

class test:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def display(self):
        print(self.id,self.name)

t=test(10,"abc")
t.display 