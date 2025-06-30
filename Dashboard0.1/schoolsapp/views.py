from django.shortcuts import render
from .models import TeacherInfo

def teacher_list(request):
    specific_entries = {
        'entry_1': TeacherInfo.objects.get(id=1),  # Fetch the entry with ID 1
        'entry_2': TeacherInfo.objects.get(id=2),  # Fetch the entry with ID 2
        'entry_3': TeacherInfo.objects.get(id=3),  # Fetch the entry with ID 3
        'entry_4': TeacherInfo.objects.get(id=2),  # Fetch the entry with ID 4
        'entry_5': TeacherInfo.objects.get(id=5),  # Fetch the entry with ID 5
        'entry_6': TeacherInfo.objects.get(id=6),  # Fetch the entry with ID 6
        'entry_7': TeacherInfo.objects.get(id=7),  # Fetch the entry with ID 7
        'entry_8': TeacherInfo.objects.get(id=8),  # Fetch the entry with ID 8
        

    }
    return render(request, "schools.html", {'specific_entries': specific_entries})

 