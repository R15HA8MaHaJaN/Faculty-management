from django.urls import path
from . import views

app_name = 'Facultyapp'


urlpatterns = [
    path('faculty/', views.facultypage, name='faculty'),
]
