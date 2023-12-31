from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.views import View
from django.contrib import messages


# Create your views here.

class LogoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,"Logged out successfully")
        return redirect('login')

class LoginView(View):
    def get(self,request):
        return render(request,'accounts/login.html')

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request,"Login succesfully")
            return redirect('task-show')
        messages.error(request,"Login fail ...")
        return redirect ('login')
    


class RegisterView(View):
    def get(self,request):
        return  render(request,'accounts/register.html')
    
    def post(self,request):             
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = User.objects.create_user(username=username,email=email,password=password)
        if user is not None:
            user.first_name=first_name
            user.last_name=last_name
            user.is_active= True
            user.save()
            return redirect('login')
        return redirect('register')
            