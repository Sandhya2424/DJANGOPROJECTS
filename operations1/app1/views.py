from django.shortcuts import render

from app1.forms import AdditionForm

def addition(request):
    if (request.method=="POST"):
        print(request.POST)   #submitted data
        #creating form_instance using submitted data
        form_instance=AdditionForm(request.POST)
        #check whether the data is valid
        if form_instance.is_valid():

            #process data
            data=form_instance.cleaned_data    #validated data
            print(data)
            n1=data['num1']
            n2=data['num2']
            s=int(n1)+int(n2)
            context={'result':s,'form':form_instance}

        return render(request,'addition.html',context)


    if(request.method=="GET"):
        form_instance=AdditionForm()     #empty form object
        context={'form':form_instance}
        return render(request,'addition.html',context)


from app1.forms import BMIForm

def bmi(request):
    if request.method == "POST":
        print(request.POST)  # submitted data
        # create form_instance using submitted data
        form_instance=BMIForm(request.POST)
        # check whether the data is valid
        if form_instance.is_valid():
            # process data
            data = form_instance.cleaned_data  # validated data
            print(data)

            height= data['height']
            weight= data['weight']


            height= height/ 100
            # calculate BMI
            bmi=weight/(height ** 2)

            # round BMI to 2 decimal places
            bmi=round(bmi, 2)

            # optional: classify BMI
            if bmi < 18.5:
                status = "Underweight"
            elif 18.5 <= bmi < 24.9:
                status = "Normal weight"
            elif 25 <= bmi < 29.9:
                status = "Overweight"
            else:
                status = "Obese"

            context = {'result': bmi,'status': status,'form': form_instance}
            return render(request, 'bmi.html', context)

    if request.method == "GET":
        form_instance = BMIForm()  # empty form object
        context = {'form': form_instance}
        return render(request, 'bmi.html', context)



from app1.forms import SignupForm

def signup(request):
    if request.method=="POST":
        print(request.POST)
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)                           # you can optionally process or save data here

            context = {'form':form_instance,'message':"Signup successful!",'data':data,}
            return render(request, 'signup.html', context)

    form_instance=SignupForm()
    context={'form':form_instance}
    return render(request,'signup.html',context)

from app1.forms import CalorieForm

def calorie(request):
    if request.method=="POST":
        print(request.POST)
        form_instance=CalorieForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)                           # you can optionally process or save data here

            w=int(data['weight'])
            h=int(data['height'])
            a=int(data['age'])
            g=data['gender']
            al=float(data['Activity_Level'])

            if g=="male":
                bmr=10*w+6.25*h-5*a+5
            else:
                bmr=10*w+6.25*h-5*a-161
            print(bmr)
            c=bmr*al
            print(c)
            context={'result':c,'form':form_instance}
            return render(request, 'calorie.html', context)

    form_instance=CalorieForm()
    context={'form':form_instance}
    return render(request,'calorie.html',context)

