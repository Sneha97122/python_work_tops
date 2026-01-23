class emp:
    def __init__(self,name,email,phone):
        self.__name=name
        self._email=email
        self.phone=phone

class company:
    def display(self):
        print()

e=emp("sneha","s@gmial.com",1234567890)
print(e.phone)
print(e._email)
# print(dir(e))
print(e._emp__name)

c=company()
c.display() 

















