from django import forms
from .models import Projects


class ProjectModelForm(forms.ModelForm):
    class Meta:
        model=Projects
        fields="__all__"
        widgets={
        "title":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Title"}),
        "description":forms.Textarea(attrs={"class":"form-control","placeholder":"Enter description"}),
        "language":forms.TextInput(attrs={"class":"form-control"}),
        # "image":forms.FileInput(attrs={"class":"form-control"})
        }