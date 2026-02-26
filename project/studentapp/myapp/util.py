from faker import Faker
import random
fake = Faker()
from myapp.models import *

def gen(n=50):
    depts=Dept.objects.all()
    for i in range(n):
        dept=depts[random.randint(0,len(depts)-1)]
        name=fake.name()
        email=fake.email()
        age=random.randint(21,30)
        stid= f"STD_{(random.randint(100,999))}"
        stobj=StudentId.objects.create(stid=stid)
        Student.objects.create(dept=dept,student_id=stobj,name=name,email=email,age=age)

def marks():
        students=Student.objects.all()
        for student in students:
            subject=Subject.objects.all()
            for sub in subject:
                Marks.objects.create(student=student,subject=sub,marks=random.randint(1,50))
























