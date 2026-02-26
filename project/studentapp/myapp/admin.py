from django.contrib import admin
from myapp.models import *

# Register your models here.



admin.site.register(Dept)
admin.site.register(StudentId)

class studentdata(admin.ModelAdmin):
    list_display=["dept","student_id","name","email","age"]
admin.site.register(Student,studentdata)

class subjectdata(admin.ModelAdmin):
    list_display=["name"]
admin.site.register(Subject,subjectdata)

class marksdata(admin.ModelAdmin):
    list_display=["student","subject","marks"]
admin.site.register(Marks,marksdata)

