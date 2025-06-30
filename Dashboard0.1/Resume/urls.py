from django.urls import path
from . import views

app_name = 'Resume'


urlpatterns = [
    path('resume/', views.resumepage, name='resume'),
]
