try:
    f=open("myfile3.txt","r")
    a=int(input("enter first number:-"))
    b=int(input("enter second number:-"))
    print("result=",a/b)
except ZeroDivisionError:
    print("number cant divid by zero")
except ValueError:
    print("only numberic values are allow")
except FileNotFoundError:
    print("file not flund ")