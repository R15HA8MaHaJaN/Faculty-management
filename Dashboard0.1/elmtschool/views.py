from django.shortcuts import render


# Create your views here.

def dashboardABS(request):
    return render(request, 'dashboardABS.html')


def dashboardAIB(request):
    return render(request, "dashboardAIB.html")


def dashboardAIITASET(request):
    return render(request, "dashboardAIITASET.html")


def dashboardALS(request):
    return render(request, "dashboardALS.html")


def dashboardASAP(request):
    return render(request, "dashboardASAP.html")


def dashboardASCO(request):
    return render(request, "dashboardASCO.html")


def dashboardASFT(request):
    return render(request, "dashboardASFT.html")


def dashboardASL(request):
    return render(request, "dashboardASL.html")

