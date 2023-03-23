from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "vad":"this is sent "
    }
        
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contacts(request):
    return render(request,'contacts.html')

# compiler comes here due to refference of the urls.py of home app