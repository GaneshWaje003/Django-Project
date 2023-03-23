from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "vad":"this is sent "
    }
        
    return render(request,'index.html')

def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("services")

def contacts(request):
    return HttpResponse("this is about page")

# compiler comes here due to refference of the urls.py of home app