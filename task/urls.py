from django.urls import path
from .views import DashboardView,AddtaskView,DeleteTaskView,EditTaskView


urlpatterns =[
    path('dash',DashboardView.as_view(),name='dashboard'),
    path('add',AddtaskView.as_view(),name='add'),
    path('delete/<int:id>',DeleteTaskView.as_view(),name='delete'),
    path('edit//<int:id>',EditTaskView.as_view(),name='edit'),
]