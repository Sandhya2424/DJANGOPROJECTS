from django.shortcuts import render,redirect
from django.views import View
from users.forms import SignupForm

from users.models import CustomUser


class Home(View):
    def get(self,request):
        return render(request,'home.html')
from django.core.mail import send_mail
class Register(View):
    def post(self,request):
        print(request.POST)
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            u=form_instance.save(commit=False)
            u.save()
            u.generate_otp()
            send_mail(
                "Django Auth OTP",
                 u.otp,
                "sandhyasivankunnu@gmail.com",
                [u.email],
                fail_silently=False,
            )
            return redirect('users:verification')
        else:
            print('error')
            return render(request,'register.html',{'form':form_instance})

    def get(self,request):
        form_instance=SignupForm()
        context={'form':form_instance}
        return render(request,'register.html',context)


from users.forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

class Userlogin(View):
    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            u=form_instance.cleaned_data['username']
            p=form_instance.cleaned_data['password']
            user=authenticate(username=u,password=p)
                 #authenticate() returns user object if user with the given username and password exists
                    #else returns none
            if user and user.is_superuser==True:    #if user exists
                login(request,user)   #login() adds the current user into session
                return redirect('users:adminhome')
            elif user and user.role=='student':
                login(request, user)
                return redirect('users:studenthome')
            elif user and user.role=='teacher':
                login(request, user)
                return redirect('users:teacherhome')
            else:
                messages.error(request,'invalid user credentials')
                return render(request,'login.html',{'form':form_instance})

    def get(self, request):
        form_instance=LoginForm()
        context={'form':form_instance}
        return render(request, 'login.html',context)


class Userlogout(View):
    def get(self, request):
        logout(request)
        return redirect('users:home')

class Adminhome(View):
    def get(self,request):
        return render(request,'adminhome.html')

class Studenthome(View):
    def get(self,request):
        return render(request,'studenthome.html')


class Teacherhome(View):
    def get(self,request):
        return render(request,'teacherhome.html')

class Verification(View):
    def post(self,request):
        otp=request.POST['otp']
        try:
            u=CustomUser.objects.get(otp=otp)
            u.is_verified=True
            u.is_active=True
            u.otp=None
            u.save()
            return redirect('users:login')
        except:  #if user does not exist
            messages.error(request,'invalid otp')
            return redirect('users:verification')
    def get(self, request):
        return render(request, 'verification.html')

