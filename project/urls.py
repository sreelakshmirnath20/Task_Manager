from django.urls import path
from .views import *


urlpatterns=[
    path('pdash',ProjectDashboardView.as_view(),name='pdash'),
    path('addp',AddProjectView.as_view(),name='addp')


]