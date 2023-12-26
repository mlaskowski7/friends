from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def loginView(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username=data['username'],password=data['password'])
            if user is not None:
                login(request,user)
                return HttpResponse("user authenticated and logged in")
            else:
                return HttpResponse("Invalid login")

    else:
        form = LoginForm()



    return render(request,'users/login.html',{'form':form})

@login_required 
def indexView(request):
    return render(request,'users/index.html')