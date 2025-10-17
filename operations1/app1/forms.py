from django import forms

class AdditionForm(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()



class BMIForm(forms.Form):
    height=forms.FloatField(label="Height (cm)")
    weight=forms.FloatField(label="Weight (kg)")


class SignupForm(forms.Form):
    gender_choices=(('male','Male'),('female','Female'))
    role_choices=(('admin', 'Admin'), ('student','Student'))
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    place=forms.CharField()
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
    role=forms.ChoiceField(choices=role_choices)
    email=forms.EmailField()



class CalorieForm(forms.Form):
    gender_choices=(('male','Male'),('female','Female'))
    Activity_choices=((1.2, 'Sedentary'), (1.3,'Lightly Active'),(1.55, 'Moderately Active'),(1.72, 'Very Active'),(1.9, 'Extra Active'))
    gender=forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect)
    weight=forms.FloatField()
    height=forms.FloatField()
    age=forms.IntegerField()
    Activity_Level=forms.ChoiceField(choices=Activity_choices)
