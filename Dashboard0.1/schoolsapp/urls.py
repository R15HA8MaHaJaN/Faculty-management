from django.urls import path
from . import views


app_name = 'schoolsapp'
urlpatterns = [
    
    path("schools/", views.teacher_list, name='schools'),

]
