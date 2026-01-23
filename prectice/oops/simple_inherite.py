class animal:
    name="generic"
    def display(self):
        print("genrice voice")

class cat(animal):
    def display(self):
        print("name:",self.name)

c=cat()
c.display()