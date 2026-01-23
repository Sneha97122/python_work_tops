class pen():
    price=10
    colour="black"

    def write(self):
        
        print("writing somting...")
        print(self.price,self.colour)

    def display(self):
        print(self.price,self.colour)

p1=pen()
p1.price=20
p1.colour="red"
p1.write()

p2=pen()
p2.price=150
p2.display()
