"""
URL configuration for Dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from elmtschool.views import *
from schoolsapp.views import *   
from Facultyapp.views import *   
from Resume.views import *   
from django.conf import settings
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('schoolsapp.urls')),
    path('', include('elmtschool.urls')),
    path('', include('Facultyapp.urls')),
    path('', include('Resume.urls')),
    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        # ... your existing URL patterns ...
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
