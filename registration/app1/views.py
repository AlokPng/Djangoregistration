from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.



def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass01=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass01!=pass2:
            return HttpResponse("oops!, password doesn't match")
        else:
            my_user=User.objects.create_user(uname,email,pass01)
            my_user.save()
            return redirect('login')

         
    return render (request,'signup.html')

def loginp(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        print(username,pass1)
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('email or username is incorrect')
    return render(request,'login.html')    
@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

def logoutp(request):
    logout(request)
    return redirect('login')