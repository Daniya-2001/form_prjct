from django.shortcuts import render, redirect
from datetime import date
import random
from .models import *




# Create your views here.

def Index(request):
    
    return render(request, 'index.html')

def FormVali(request):
    if request.method == 'POST':
        Name = request.POST.get('username')
        DOB = request.POST.get('dob')
        birth_year, birth_month, birth_day = map(int, DOB.split('-'))
        today = date.today()
        age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
        Phone = request.POST.get('mobile')
        About = request.POST.get('about')
        Email = request.POST.get('mail')
        userform = UserForm()
        userform.Name = Name
        userform.Age = age
        userform.Phone = Phone
        userform.Email = Email
        userform.About = About
        userform.save()
        
    return redirect('secondform') 

def SecondForm(request):
    userId = random.randint(99, 999)
    return render(request, 'secondform.html', {"value" : userId})