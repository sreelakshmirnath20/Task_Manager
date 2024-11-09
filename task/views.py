from django.shortcuts import render,redirect
from django.views import View
from .forms import Taskform
from django.http import HttpResponse
from .models import Task

# Create your views here.

# def landingView(reqest):
#     return render(reqest,"landing.html")

class LandingView(View):
    def get(self,request):
        return render(request,"landing.html")

# def dashboardView(request):
#     return render(request,"dashboard.html")
class DashboardView(View):
    def get(self,request):
        data=Task.objects.all()
        return render(request,"dashboard.html",{"data":data})
    
class AddtaskView(View):
    def get(self,request):
        form=Taskform()
        return render(request,'add.html',{"form":form})
    def post(self,request):
        formdata=Taskform(data=request.POST)
        if formdata.is_valid():
            # print(formdata.cleaned_data)
            title=formdata.cleaned_data.get('title')
            dec=formdata.cleaned_data.get('description')
            dt=formdata.cleaned_data.get('date')
            tm=formdata.cleaned_data.get('time')
            Task.objects.create(title=title,description=dec,date=dt,time=tm)
            return redirect('dashboard')
        return render(request,'add.html',{"form":formdata})
    
class DeleteTaskView(View):
    def get(self,request,*args,**kwargs):
        tid=kwargs.get('id')
        print(tid)
        task=Task.objects.get(id=tid)
        task.delete()
        return redirect('dashboard')
    

class EditTaskView(View):
    def get(self,request,**kwargs):
        tid=kwargs.get('id')
        task=Task.objects.get(id=tid)
        form=Taskform(initial={"title":task.title,"description":task.description,"date":task.date,"time":task.time})
        return render(request,"edit.html",{"form":form})
    def post(self,request,**kwargs):
        formdata=Taskform(data=request.POST)
        tid=kwargs.get('id')
        task=Task.objects.get(id=tid)
        if formdata.is_valid():
            title=formdata.cleaned_data.get('title')
            dec=formdata.cleaned_data.get('description')
            dt=formdata.cleaned_data.get('date')
            tm=formdata.cleaned_data.get('time')
            task.title=title
            task.description=dec
            task.date=dt
            task.time=tm
            task.save()
            return redirect('dashboard')
        return render(request,"edit.html",{"form":formdata})




