from django.db.transaction import commit
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app1.forms import SignupForm, LoginForm,SchoolForm


class Home(View):
    def get(self, request):
        return render(request, 'home.html')


class Register(View):
    def post(self, request):
        form_instance = SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('home')
        else:
            messages.error(request, 'Registration failed')
            return render(request, 'register.html', {'form': form_instance})

    def get(self, request):
        form_instance = SignupForm()
        context = {'form': form_instance}
        return render(request, 'register.html', context)


class Userlogin(View):
    def post(self, request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
            u = form_instance.cleaned_data['username']
            p = form_instance.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user:
                login(request, user)
                if user.is_superuser:
                    return redirect('adminhome')
                else:
                    return redirect('studenthome')
            else:
                messages.error(request, 'Invalid user credentials')
                return render(request, 'login.html', {'form': form_instance})

    def get(self, request):
        form_instance = LoginForm()
        context = {'form': form_instance}
        return render(request, 'login.html', context)


class Userlogout(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class Adminhome(View):
    def get(self, request):
        return render(request, 'adminhome.html')


class Studenthome(View):
    def get(self, request):
        return render(request, 'studenthome.html')


class Addschool(View):
    def post(self, request):
        form_instance = SchoolForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('home')
        else:
            messages.error(request, 'failed to add book')
            return render(request, 'addschool.html', {'form': form_instance})

    def get(self, request):
        form_instance = SchoolForm()
        context = {'form': form_instance}
        return render(request, 'addschool.html', context)

from app1.models import School

class Schoollist(View):
    def get(self, request):
        schools=School.objects.all()
        return render(request, 'schoollist.html', {'schools': schools})


from app1.models import Student
class Schooldetail(View):
    def get(self, request, i):
        s=School.objects.get(id=i)

        can_join=True
        is_student=False
        try:
            u=request.user
            st=Student.objects.get(user=u)
            can_join=False
            if st.school==s:
                is_student=True
        except:
            pass
        context={'school':s,'can_join':can_join,'is_student':is_student}

        return  render(request,'schooldetail.html',context)





from app1.forms import StudentjoinForm
class StudentJoin(View):
    def get(self, request,i):
        form_instance=StudentjoinForm()
        context={'form':form_instance}
        return render(request,'studentjoin.html',context)

    def post(self,request,i):
        form_instance=StudentjoinForm(request.POST)
        if form_instance.is_valid():
            st=form_instance.save(commit=False)    #to add additional field set commit=false
            sc=School.objects.get(id=i)            #retrieve the school object
            st.school=sc                           #assigns selected school object to student school field
            u=request.user                         #retrieve the current user object from section
            st.user=u                              #assigns the logged user object to student user field
            st.save()                               #then saves the student record
            return redirect('studenthome')



class LeaveSchool(View):
    def get(self, request, i):
        u=request.user
        s=School.objects.get(id=i)
        try:
            st=Student.objects.get(user=u,school=s)
            st.delete()
        except:
            pass
        return redirect('schooldetail',i=i)
