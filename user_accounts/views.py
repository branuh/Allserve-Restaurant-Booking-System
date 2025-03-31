from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm

# create your views here
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("login")
    else:
        form = CustomUserCreationForm
    return render(request,'user_accounts/register.html',{'form':form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        #check if a user with above credentials exist in the system
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("todoapp")
        else:
            messages.error(request, "Invalid username or password")
    return render(request,'user_accounts/login.html')

#if user is not logged in our db login_required decorator redirects them back to login page
#else we will allow them to see our home page
@login_required
def home_view(request):
    return render(request, 'user_accounts/home.html')

def logout_view(request):
    logout(request)
    return redirect("login")
        




