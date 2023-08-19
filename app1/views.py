from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    return render(request, 'a.html', {'titles': 'Django', 'link': 'http://127.0.0.1:8000/'})

def profile(request):
    return render(request, 'a.html', {'titles': 'profile page', 'link': 'http://127.0.0.1:8000/'})

def expression(request):
    a=int(request.POST['text1'])
    b=int(request.POST['text2'])
    c=a+2*b
    return render(request, 'output.html', {'result':c})

def signup(request):
    return render(request, 'signup.html', {'titles':'SignUp','link':'http://127.0.0.1:8000/'})