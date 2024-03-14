from django.shortcuts import render,redirect
from . models import*
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import json
from app.forms import CustomUserForm

def home(request):
    return render(request,"index.html")

def register_page(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Succes you can login now...!")
            return redirect('/login_page')
    return render(request,"register.html",{'form':form})

            
def login_page(request):
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password")
                return redirect("/login_page")
        return render(request,"login.html")