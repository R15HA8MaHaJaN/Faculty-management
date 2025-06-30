from django.urls import path
from . import views


app_name = 'elmtschool'
urlpatterns = [
    path('dashboardASL',views.dashboardASL, name = 'dashboardASL'),
    path('dashboardASFT',views.dashboardASFT, name = 'dashboardASFT'),
    path('dashboardASCO',views.dashboardASCO, name = 'dashboardASCO'),
    path('dashboardASAP',views.dashboardASAP, name = 'dashboardASAP'),
    path('dashboardALS',views.dashboardALS, name = 'dashboardALS'),
    path('dashboardAIITASET',views.dashboardAIITASET, name = 'dashboardAIITASET'),
    path('dashboardAIB',views.dashboardAIB, name = 'dashboardAIB'),
    path('dashboardABS',views.dashboardABS, name = 'dashboardABS'),
]
