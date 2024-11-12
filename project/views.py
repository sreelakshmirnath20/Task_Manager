from django.shortcuts import render,redirect
from django.views import View
from .forms import ProjectModelForm
from .models import Projects
from django.contrib import messages

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
            messages.success(request,"Project Added Successfully !!")
            messages.error(request,"Checking")
            return redirect('pdash')
        return render(request,"addproject.html",{'form':formdata})

class DeleteTaskView(View):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get('id')
        print(pid)
        project=Projects.objects.get(id=pid)
        project.delete()
        return redirect('pdash')
    
class EditProjectView(View):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get('pid')
        print('pid')
        project=Projects.objects.get(id=pid)
        form=ProjectModelForm(instance=project)
        return render(request,"editpro.html",{"form":form})
    def post(self,request,**kwargs):
        pid=kwargs.get('pid')
        project=Projects.objects.get(id=pid)
        formdata=ProjectModelForm(data=request.POST,files=request.FILES,instance=project)
        if formdata.is_valid():
            formdata.save()
            messages.success(request,"Project updated Successfully !!")
            return redirect('pdash')
        return render(request,"editpro.html",{"form":formdata})





