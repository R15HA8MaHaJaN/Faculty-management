from django.shortcuts import render

# Create your views here.

def resumepage(request):
    return render(request, 'resume.html')