from django.shortcuts import render
from myapp.models import *
from django.core.paginator import Paginator
from django.db.models import Sum
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import requests

# Create your views here.

def index(request):
    students=Student.objects.all()
    paginator=Paginator(students,7)

    page_number=request.GET.get("page")
    page_obj=paginator.get_page(page_number)

    return render(request,"index.html",{"students":page_obj})

def reportcard(request):
    sid=request.GET['sid']
    action=request.GET['action']
    Student.objects.get(pk=sid)
    student=Student.objects.filter(student_id = sid)
    marks=Marks.objects.filter(student_id=sid)

    total= 0
    for m in marks:
        total+=m.marks

    per=(total*100)/250


    students = Student.objects.annotate(total_marks=Sum('marks__marks')).order_by('total_marks')
    for st in students:
        print(st.total_marks,st.id)
        if int(st.id) == int(sid):
            break

    rank = 0
    for st in students:
        rank+=1       
        if int(st.id)==int(sid):
            break

    if action=='card':

        return render(request,"reportcard.html",{"students":student,"marks":marks,"total":total,"per":per,"rank":rank})
    else:
         html_content = render_to_string('reportcard.html', {"marks":marks,"total":total,"per":per,"rank":rank})
         text_content = strip_tags(html_content)

         send_mail(
            'Subject',
            text_content, 
            settings.DEFAULT_FROM_EMAIL,
             [marks[0].student.email],
            html_message=html_content, 
        )
    return render(request,"reportcard.html",{"marks":marks,"total":total,"per":per,"rank":rank})


