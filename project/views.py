from django.shortcuts import render
from django.views import View
from .forms import ProjectModelForm

# Create your views here.

class ProjectDashboardView(View):
    def get(self,request):
        return render(request,"pdashboard.html")
    
class AddProjectView(View):
    def get(self,request):
        form=ProjectModelForm()
        return render(request,"addproject.html",{"form":form})





