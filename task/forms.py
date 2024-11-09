from django import forms


class Taskform(forms.Form):
    title=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form_control","palceholder":"Enter Title"}))
    description=forms.CharField(max_length=1000,widget=forms.Textarea(attrs={"class":"form-control"}))
    date=forms.DateField(widget=forms.SelectDateWidget(attrs={"class":"form-control"}))
    time=forms.TimeField(widget=forms.TimeInput(attrs={"class":"form-control"}))