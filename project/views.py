from django.shortcuts import render,redirect
from django.views import View
from .forms import ProjectModelForm
from .models import Projects

# Create your views here.

class ProjectDashboardView(View):
    def get(self,request):
        data=Projects.objects.all()
        return render(request,"pdashboard.html",{"projects":data})
    
class AddProjectView(View):
    def get(self,request):
        form=ProjectModelForm()
        return render(request,"addproject.html",{"form":form})
    def post(self,request):
        formdata=ProjectModelForm(data=request.POST,files=request.FILES)
        if formdata.is_valid():
            formdata.save()
            return redirect('pdash')
        return render(request,"pdashboard.html",{'form':formdata})

class DeleteTaskView(View):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get('id')
        print(pid)
        project=Projects.objects.get(id=pid)
        project.delete()
        return redirect('pdash')
    
class EditProjectView():
    def get(self,request,*args,**kwargs):
        pid=kwargs.get('pid')
        project=Projects.objects.get(id=pid)
        form=ProjectModelForm(instance=project)
        return render(request,"editpro.html",{"form":form})





