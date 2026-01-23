class a:
    def __display(self):
        print("a is caaling")

class b(a):
    def display(self):
        print("b is calling")

b=b()
b.display()
