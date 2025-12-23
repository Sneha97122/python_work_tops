
choise ='yes'
while choise == 'yes':
    marks=int(input("enter your marks"))
    if marks>=90 and marks<=100:
        print("YOUR GREAD IS A+")
    elif marks>=80 and marks<=90:
        print("YOUR GRADE IS A")
    elif marks >=70 and marks<=80:
        print("YOUR GRADE IS B")
    elif marks >=60 and marks<=70:
        print("YOUR GRADE IS C")
    elif marks >= 50 and marks<=60:
     print("YOUR GRADE IS D")
    elif marks >=40 and marks<=30:
        print("YOUR GRADE IS E")
    elif marks <=30:
        print("YOU ARE FAIL ")
    else :
        print("wrong choise")
    choise =input("do you want to re-enter marks(y/n):")



       