from django.shortcuts import render
from django.views import View

# Create your views here.

class ProjectDashboardView(View):
    def get(self,request):
        return render(request,"pdashboard.html")
    
class AddProjectView(View):
    def get(self,request):
        return render(request,"addproject.html")





