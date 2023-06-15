from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def landing_page(request):
    return render(request, 'landingpage.html', {})

def login_page(request):
    return render(request,'login.html',{})

def signup_page(request):
    return render(request,'signup.html',{})
def water_view(request):
    return render(request,'water.html',{})
