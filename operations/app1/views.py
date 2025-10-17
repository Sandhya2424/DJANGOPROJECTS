from django.shortcuts import render


from django.shortcuts import render
def addition(request):
    if(request.method == 'POST'):
        print(request.POST)
        n1=int(request.POST['n1'])
        n2=int(request.POST['n2'])
        s=n1+n2
        context={'result':s}
        return render(request,'addition.html',context)

    if(request.method == "GET"):
        return render(request, 'addition.html')

def factorial(request):
    if(request.method == 'POST'):
        print(request.POST)
        n=int(request.POST['n1'])
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        context={'result':fact}
        return render(request,'factorial.html',context)

    if(request.method == "GET"):
        return render(request, 'factorial.html')


from django.shortcuts import render


def bmi(request):
    if (request.method == 'POST'):
        weight=float(request.POST['weight'])
        height=float(request.POST['height'])
        bmi_value=weight/(height*height)
        if bmi_value<=18.4:
            bmi_category="Underweight"
        elif 18.5<=bmi_value<=24.9:
            bmi_category="Normal"
        elif 25.0<=bmi_value<=39.9:
            bmi_category="Overweight"
        elif bmi_value>=40.0:
            bmi_category="Obese"
        else:
            bmi_category="Invalid BMI"

        context = {'bmi_value':bmi_value,'bmi_category':bmi_category}
        return render(request, 'bmi.html',context)

    if (request.method == "GET"):
        return render(request, 'bmi.html')
