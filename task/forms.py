from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Taskform(forms.Form):
    title=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form_control","palceholder":"Enter Title"}))
    description=forms.CharField(max_length=1000,widget=forms.Textarea(attrs={"class":"form-control"}))
    date=forms.DateField(widget=forms.SelectDateWidget(attrs={"class":"form-control"}))
    time=forms.TimeField(widget=forms.TimeInput(attrs={"class":"form-control"}))

class Logform(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control"}))

class Regform(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]