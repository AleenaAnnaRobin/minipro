from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import View

# Create your views here.
from django.shortcuts import render

def landing_page(request):
    return render(request, 'landingpage.html', {})

def login_page(request):
    return render(request,'login.html',{})

def signup_page(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}

    return render(request,'signup.html',context)
def water_view(request):
    return render(request,'water.html',{})

def profile_view(request):
    return render(request,'profile.html',{})

class RegisteredUser(View):
    def post
