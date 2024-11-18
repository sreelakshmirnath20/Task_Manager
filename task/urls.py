from django.urls import path
from .views import DashboardView,AddtaskView,DeleteTaskView,EditTaskView,LandingView,RegView


urlpatterns =[
    path('dash',DashboardView.as_view(),name='dashboard'),
    path('add',AddtaskView.as_view(),name='add'),
    path('landing',LandingView.as_view(),name='landing'),
    path('reg',RegView.as_view(),name='reg'),


    path('delete/<int:id>',DeleteTaskView.as_view(),name='delete'),
    path('edit//<int:id>',EditTaskView.as_view(),name='edit'),
]