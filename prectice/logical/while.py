#from user input
num=int(input("enter the number:"))
fact =1
i=num

while i in range (num,0,-1):
    fact*=i
    i -=1
print(fact)


#without user input
num=5
fact=1
i=num
while i>0:
    fact*=i
    i-=1
print(fact)

    