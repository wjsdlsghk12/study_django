from django.shortcuts import render

def home(request):
    return render(request,'index.html')

# Create your views here.

def text(request,string):
    return render(request,'text.html',{'fucking':string})