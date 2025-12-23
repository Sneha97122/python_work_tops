try :
    a=10
    b=a/4
    print(b)
except Exception as e:
    print(e)
else:
    print("something...")

finally:
    print("always execute")


