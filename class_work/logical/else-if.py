choise='y'
while choise=='y':
    marks = int(input("enter you marks:"))
    if marks>91 and marks<100:
        print("your grade is a  ")
    elif marks>71 and marks<90:
        print("your grade is b")
    elif marks>51 and marks<70:
        print("your grade is c")
    elif marks>35 and marks<50:
        print("your grade is d")
    elif marks>0 and marks<34:
        print("your fail")
    else:
        print("wrong input")
    choise = input("do you want to re-enter maerks(y/n):")





