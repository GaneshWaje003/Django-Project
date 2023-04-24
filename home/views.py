from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contacts(request):
    return render(request,'contacts.html')

def login(request):
    return render(request,'new_login.html')

def java(request):
    return render(request,'java.html')

# compiler comes here due to refference of the urls.py of home app