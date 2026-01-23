
x=10

class tops:
    def show(self):
        x=20
        print("local:",x)
        print("global",globals()['x'])

t=tops()
t.show()
    