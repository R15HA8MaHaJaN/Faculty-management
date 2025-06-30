from django.db import models

# Create your models here.

from django.db import models


class TeacherInfo(models.Model):
    
    category = models.CharField(max_length=20, blank=True, null=True)
    faculties_required = models.IntegerField(blank=True, null=True)
    faculties_available = models.IntegerField(blank=True, null=True)
    deficiency = models.IntegerField(blank=True, null=True)
    approval_uploaded = models.IntegerField(blank=True, null=True)
    cvs_available = models.CharField(db_column='CVs_available', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    interview_scheduled = models.DateField(db_column='interview_Scheduled', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Schools_TeacherInfo'