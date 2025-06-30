from django.shortcuts import render

# Create your views here.

def facultypage(request):
    return render(request, 'faculty.html')