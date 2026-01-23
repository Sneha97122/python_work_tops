from multipledispatch import dispatch

class cala:

    @dispatch(int,int)
    def add(self,a,b):
        print(f"addition is:-{a+b}")

    @dispatch(int,int,int)
    def add(self,a,b,c):
        print(f"addition is:-{a+b+c}")


    # def add(*a):
    #     sum=0
    #     for i in a:
    #         sum+=i

c=cala()
c.add(10,20,30)