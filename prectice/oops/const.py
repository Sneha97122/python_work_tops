class test:
    def __init__(self,id,name):
        print("constructor calling..")
        self.id=id
        self.name=name

    def display(self):
        print("calling display")
        print(self.id,self.name)

t1=test(101,"sneha")
t1.display()

t2=test(102,"dishu")
t2.display()