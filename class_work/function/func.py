def messege():
    print("hello sneha good morning")

messege()

def add(a):
    print(f"squer of {a} is {a*a}")

add(10)

def sum(a,b):
    print(f"sum of {a} and {b} is {a+b}")

sum(10,20)

def mod(a,b):
    c=a%b
    return c

print(mod(10,2))

def num(*a):
    print(a)

num(10,20,30)

def num1(**a):
    print(a)

num1(name='sneha',email='sneha@gmail.com')

def person(name,email,phone):
    print(name,email,phone)

person('sneha','s@gmail.com',123456789)


k=lambda a,b:a+b
print(k(10,20))

sqr=lambda a,b :a*b
print(sqr(10,20))

a=10

def num():
    global a
    a=20
    print(a)

print(a)
num()
print(a)

def square(a):
    print(a*a)
    a+=1
    if a<20:
        square(a)

square(10)




