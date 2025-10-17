from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

def home(request):
    return render(request, 'home.html')

def add_employee(request):
    if request.method == "POST":
        form_instance = EmployeeForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('app1:employee_list')
    if (request.method == "GET"):
        form_instance = EmployeeForm()
        context = {'form': form_instance}
        return render(request, 'add_employee.html', context)

def employee_list(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employee_list.html', context)

