class a:
    def a(self):
        print(" a calling")

class b(a):

    def b(self):
        print("b calling")

    def a(self):
        print("a calling-b overide")

class c(a):

    def c(self):
        print("c calling")

    def a(self):
        print("c calling")

    def a(self):
        print("a calling -c overide")

class d(c,b):

    def d(self):
        print("d calling")

d=d()
d.d()
d.a()
d.b()
d.c()