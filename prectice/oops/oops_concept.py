class student:
    clg="assc"
    def __init__(self,id,name,email):
        self.id=id
        self.name=name
        self.email=email

    def display(self):
        print("display is calling")
        print(self.id,self.name,self.email,self.clg)

    @classmethod
    def show(cls):
        print(cls.clg)

    @staticmethod
    def util():
        print("statice function is calling")


s=student(101,"sneha","s@gmail.com")
s.display()

student.show()

student.util()
