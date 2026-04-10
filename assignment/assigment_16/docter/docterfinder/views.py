from django.shortcuts import render, redirect
from .models import Doctor

def home(request):
    doctors = Doctor.objects.all()
    return render(request, 'home.html', {'doctors': doctors})

def add_doctor(request):
    if request.method == "POST":
        name = request.POST['name']
        specialty = request.POST['specialty']
        phone = request.POST['phone']
        email = request.POST['email']

        Doctor.objects.create(
            name=name,
            specialty=specialty,
            phone=phone,
            email=email
        )
        return redirect('/')

    return render(request, 'register.html')

def delete_doctor(request, id):
    Doctor.objects.get(id=id).delete()
    return redirect('/')
