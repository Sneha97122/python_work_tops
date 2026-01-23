class pen:
    def __init__(self,price,colour):
        self.price=price
        self.colour=colour

    def display(self):
        print(self.price,self.price)

class notebook(pen):
    def __init__(self,price,colour):
        super().__init__()

    def display(self):
        super().__init__()

n=notebook(105,"red")
n.display()