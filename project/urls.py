from django.urls import path
from .views import *


urlpatterns=[
    path('pdash',ProjectDashboardView.as_view(),name='pdash'),
    path('addp',AddProjectView.as_view(),name='addp'),
    path('delete/<int:id>',DeleteTaskView.as_view(),name='delpro'),
    path('editpro/<int:pid>',EditProjectView.as_view(),name='editpro'),



]