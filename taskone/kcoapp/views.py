
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Post, Usar

# Create your views here.
def home(request):
    return render(request, 'kcoapp/home.html')

def login_view(request):
    #psts = Post.objects.all()
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        
        Usar = authenticate(request, username=username, password=password)
        if Usar is not None:
            login(request, Usar)
            messages.success(request, "Logged in successfully")
            return redirect('portal')
        
    else:
 #       messages.error(request, "Invalid username or password.")
        return render(request, 'kcoapp/Login.html')

    #return render(request, 'kcoapp/Login.html')


def user_portal(request):
    #posts = Post.objects.all()
    return render(request, 'kcoapp/portal.html')
#register a new user
def user_register(request):
    
        if request.method == 'POST':
            form = UserCreationForm(request.POST)  # Create form with POST data
            if form.is_valid():
                Usar= form.save()  # Save new user to the database
                login(request, Usar)  # Log the user in after registration
                messages.success(request, "Registration successful! You are now logged in.")
                return redirect('portal')  # Redirect to home page or another page
        else:

            form = UserCreationForm()  # Display an empty form for GET requests
        return render(request, 'kcoapp/register.html', {'form': form})



@login_required
def portal_view(request):
    return render(request, 'kcoapp/portal.html')


def custom_logout_view(request):
    logout(request)  # Logs out the user
    messages.success(request, "You have been logged out.")  # Optional message
    return redirect('portal')  # Redirect to login page or any other page




def user_update(request):
    return render(request, 'kcoapp/update.html')
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('portal')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'kcoapp/update.html', {'form': form})

def user_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('portal')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'kcoapp/update.html', {'form': form})

