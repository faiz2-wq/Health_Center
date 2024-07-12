from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from doctor.forms import PatientForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def doctor(request):
    return render(request,'doctor.html')

def news(request):
    return render(request,'news.html')

def contact(request):
    return render(request,'contact.html')

def appointment(request):
    if request.method=="POST":
        form=PatientForm(request.POST)
        if form.is_valid():
                form.save()
                return HttpResponse("<h2>Patient Save SuccessFully!</h2>")
    else:
        form=PatientForm()
    return render(request, 'appointment.html',{'form':form})
