from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout ,authenticate
from django.contrib import messages
from django.contrib.auth.hashers import check_password

# Create your views here.
def login_page(request):
    if request.method=='POST':
        user_name = request.POST['username']
        user_password = request.POST['password']
        
        user =authenticate(request,username=user_name,password=user_password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid user name or password')
            return redirect('/login')
    else:
        return render(request,'account/login_page.html')

def registeruser(request):
    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        username = request.POST['username']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        email = request.POST['email']
        if pass1 != pass2:
            messages.info(request,'Passwords do not match')
            return redirect('/register')
        elif User.objects.filter(username=username).exists():
            messages.info(request,'User name already taken')
            return redirect('/register')

        else:
            user = User.objects.create_user(email=email,first_name = firstname,last_name=lastname,
                        username=username,password=pass1)
            user.save()
            login(request,user)
            return redirect('/')
    else:
        return render(request,'account/signup.html')

def logout_page(request):
    logout(request)
    return redirect('/')

def forgot_pass(request):
    if request.method=='POST':
        pass
    else:
        return render(request,'account/forgot_pass.html')