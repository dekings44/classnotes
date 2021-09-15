from django.shortcuts import render, redirect
# from ..notebooks.models import Notes
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib import messages
from .models import MyFollower

# Create your views here.









@login_required
def profile(request):
    current_user = request.GET.get('user')
    all_users = User.objects.all()
    logged_in_user = request.user.username
    user_followers = len(MyFollower.objects.filter(user=current_user))
    user_following = len(MyFollower.objects.filter(follower=current_user))
    return render(request,'accounts/profile.html', {'section' : 'profile', 'current_user' : current_user, 'all_users' : all_users})
    
    
    
def myFollowers(request):
    if request.method == 'POST':
        value = request.POST['value']
        user = request.POST['user']
        follower = request.POST['follower']
        if value == 'follow':
            follow_cnt = MyFollower.objects.create(follower = follower, user = user)
            follow_cnt.save()
        return redirect('/?user='+user)
    
    
    
def loginUser(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('accounts:profile')
        
    return render(request, 'registration/login.html')
    
def logoutUser(request):
    logout(request)
    return redirect('accounts:login')
    


def account_register(request):
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = True
            user.save()
            messages.success(request, 'Account successfully created')
            return redirect('accounts:login')
            
    else:
        registerForm = RegisterForm()
    return render(request, 'registration/register.html', {'form': registerForm})
