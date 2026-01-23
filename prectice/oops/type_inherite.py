class a:
    def __init__(self):
        print("const is callinfg")

    def display(self):
        print("a is calling")

class b:
    def __init__(self):
        print("b const is caling")

    def display(self):
        print("b is calling")

class c(a,b):
    def __init__(self):
        # super().__init__()
        a.__init__(self)
        a.__init__(self)

    def display(self):
        print("c is caaling")
        b.display(self)
        a.display(self)

c=c()
c.display()



# class a:
#     def __init__(self):
#         print("a const calling")

#     def display(self):
#         print("running a")

# class b:
#     def __init__(self):
#         print("b const calling")

#     def display(self):
#         print("b is running")

# class c(a,b):
#     def __init__(self):
#         a.__init__(self)
#         b.__init__(self)

#     def display(self):
#         print("c is cslling")
#         a.display(self)
#         b.display(self)

# c=c()
# c.display()