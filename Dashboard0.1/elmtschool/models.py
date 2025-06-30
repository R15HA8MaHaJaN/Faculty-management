from django.db import models

# Create your models here.

from django.db import models

class schoolfacultymembers(models.Model):
    
    Fullname = models.CharField(max_length=20, blank=True, null=True)
    Contact = models.IntegerField(blank=True, null=True)
    Designation  = models.IntegerField(blank=False, null=False)
    School = models.IntegerField(blank=True, null=True)
    Group = models.IntegerField(blank=False, null=False)
    
    class Meta:
        managed = True
        db_table = 'elmtschool_TeacherInfo'