class pen:
    price =10
    color="red"

    def to_write(self):
        

        print("witing somthing..")
        print(self.price,self.color)

    def display(self):
        print(self.price,self.color)

p1 =pen()
p1.to_write()
p1.display()

p2=pen()
p2.to_write()
p2.display()