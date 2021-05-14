from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect
from drive.models import Upload_model
import os
from django.conf import settings

# Create your views here.

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                messages.success(request, "Account Created Successfully")
                return redirect('login')
        else:
            messages.error(request,'Passwword and Confirm Password did not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

    return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('my_drive')
        else:
            messages.error(request, 'Invalid Login Credentials')
            return redirect('login')
    else:    
        return render(request,'login.html')

total=[1,2,3,4,5,6,7,8]
def my_drive(request):
    if request.session._session:
        return render(request,'my_drive.html',{'data':'home'})
    else:
        return render(request, 'login.html')

def all_files(request):
    if request.session._session:
        f_data= Upload_model.objects.all()
        user_data= User.objects.all()
        return render(request,'my_drive.html',{'data':'all_files', 'file_data':f_data, 'u_data':user_data})
    else:
        return render(request, 'login.html')

def photos(request):
    if request.session._session:
        f_data= Upload_model.objects.all()
        return render(request,'my_drive.html',{'data':'photos', 'file_data':f_data})
    else:
        return render(request, 'login.html')

def videos(request):
    if request.session._session:    
        f_data= Upload_model.objects.all()
        return render(request,'my_drive.html',{'data':'videos', 'file_data':f_data})
    else:
        return render(request, 'login.html')

def documents(request):
    if request.session._session:    
        f_data= Upload_model.objects.all()
        return render(request,'my_drive.html',{'data':'documents', 'file_data':f_data})
    else:
        return render(request, 'login.html')

def dashboard(request):
    if request.session._session:   
        u_data = User.objects.all() 
        return render(request,'my_drive.html',{'data':'dashboard', 'user_data':u_data})
    else:
        return render(request, 'login.html')

def upload_f(request):
    if request.session._session:    
        if request.method == 'POST':
            uploaded_file = request.FILES['uploaded_file1']
            file_data = Upload_model(uploaded_file=uploaded_file, file_name=uploaded_file.name, file_size=uploaded_file.size, file_type=uploaded_file.content_type, user_name=request.user.username)
            file_data.owner = request.user
            file_data.save();
            messages.success(request, "File Uploaded Successfully") 
            return redirect('my_drive')
        else:
            return redirect('my_drive')
    else:
        return render(request, 'login.html')

def logout(request):
    if request.session._session:
        auth.logout(request)
        return redirect('login')
    else:
        return render(request,'login.html')

def delete_user(request,pk):
    if request.session._session:
        User.objects.filter(id=pk).delete()
        messages.success(request,"User Deleted Successfully")
        return redirect('dashboard')
    else:
        return render(request,'login.html')