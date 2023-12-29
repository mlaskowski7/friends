from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserEditingForm, ProfileEditingForm
from posts.models import Post
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.

def loginView(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username=data['username'],password=data['password'])
            if user is not None:
                login(request,user)
                return render(request, 'users/validLogin.html',{'user':user})
            else:
                return render(request, 'users/invalidLogin.html')

    else:
        form = LoginForm()



    return render(request,'users/login.html',{'form':form})


class CustomLogoutView(LogoutView):
    template_name = 'users/logout.html'  

    def dispatch(self, request, *args, **kwargs):
        # Perform logout for GET requests
        logout(request)

        
        return redirect('index') 

@login_required 
def indexView(request):
    current_user = request.user
    posts = Post.objects.filter(user=current_user)
    profile = Profile.objects.filter(user=current_user).first()
    return render(request,'users/index.html', {'posts': posts,'profile':profile})

def registerView(request):
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            newUser = register_form.save(commit=False)
            newUser.set_password(register_form.cleaned_data['password'])
            newUser.save()
            Profile.objects.create(user=newUser)
            return render(request,'users/registerDone.html')
    else:
        register_form = UserRegisterForm()
    return render(request,'users/register.html',{'register_form':register_form})

@login_required
def editView(request):
    if request.method == 'POST':
        user_form = UserEditingForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditingForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditingForm(instance=request.user,data=request.GET)
        profile_form = ProfileEditingForm(instance=request.user.profile,data=request.GET,files=request.FILES)
    return render(request,'users/edit.html',{'user_form':user_form,'profile_form':profile_form})



