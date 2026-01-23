try:
    a=int(input("enter first number:-"))
    b=int(input("enter second number:-"))
    result=a/b
    print("result",result)
except ZeroDivisionError:
    print("number cant divide by zero")
except ValueError:
    print("only numbers are allowd")

else:
    print("program is done")
finally:
    print("program is end")