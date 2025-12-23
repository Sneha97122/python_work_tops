number = int(input("enter the number="))
flag = 0
for i in range(2,number):
    if number%i==0:
        flag=1
        break

if flag==0:
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")