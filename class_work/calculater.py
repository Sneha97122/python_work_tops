print("press + for addition")
print("press - for subtraction")
print("press * for multiplication")
print("press / for diversion")
print("press /%/ for module")

a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
result=0
chs='y'
while chs=='y':
    choise=input("enter your choise:")
if choise == '+':
    print("result=",a+b)
elif choise == '-':
    print('result=',a-b)
elif choise == '*':
    print('result=',a*b)
elif choise == '/':
    print('result=',a/b)
elif choise == '%':
    print('result=',a%b)

chs=input("do you want to do more  ")
# factoiral from while loop ,armstrong number of 3 digits 