from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=100,blank=False, default='')
    Project_Description = models.CharField(max_length=200, blank=False, default='')
    Project_Department = models.CharField(max_length=200, blank=False, default='')
    StartDate_pro = models.DateField()
    EndDate_pro = models.DateField()
    Created_at = models.DateTimeField(auto_now=True)
    Updated_at = models.DateTimeField(auto_now=True)
    Deleted_at = models.DateTimeField(auto_now=True)

class Resource(models.Model):
    id = models.AutoField(primary_key=True)
    ResourceName = models.CharField(max_length=100,blank=False, null=False)
    #project = models.ForeignKey(Project, on_delete=models.CASCADE, default='')
    StartDate = models.DateField()
    EndDate = models.DateField()
    Created_at = models.DateTimeField(auto_now=True)
    Updated_at = models.DateTimeField(auto_now=True)
    Deleted_at = models.DateTimeField(auto_now=True)
    '''points = models.JSONField({1:'0', 2:'0' , 3:'0' ,4:'0', 5:'0' , 6:'0', 7:'0', 8:'0' , 9:'0',
                               10: '0', 11: '0', 12: '0' , 13:'0', 14:'0' , 15:'0',
                               16: '0', 17: '0', 18: '0' , 19:'0', 20:'0' , 21:'0',
                               22: '0', 23: '0', 24: '0' , 25:'0', 26:'0' , 27:'0',
                               28: '0', 29: '0', 30: '0' , 31:'0'}, default=0)'''
    # Availablity = models.DecimalField(max_digits=2, decimal_places=1)

class ResourceAllocation(models.Model):
    # id = models.IntegerField(primary_key=True)
    Project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    Resource_id = models.ForeignKey(Resource, on_delete=models.CASCADE)
    StartDate_all = models.DateField()
    EndDate_all = models.DateField()
    # ProjectName = models.ForeignKey(Project, on_delete=models.CASCADE)
    # ResourceName = models.ForeignKey(Resource, on_delete=models.CASCADE)
    year = models.IntegerField()
    month = models.IntegerField()
    points = models.CharField(max_length=4)
    StartDay_all = models.IntegerField()
    EndDay_all = models.IntegerField()
    Created_at = models.DateTimeField(auto_now=True)
    Updated_at = models.DateTimeField(auto_now=True)
    Deleted_at = models.DateTimeField(auto_now=True)


class Login(models.Model):
    username=models.CharField(max_length=10,blank=False, default='')
    password = models.CharField(max_length=10,blank=False, default='')

class DateSave(models.Model):
    Allocation_id = models.ForeignKey(ResourceAllocation, on_delete=models.CASCADE)
    Day = models.DateField()
    DayValue = models.CharField(max_length=4)
    day_week= models.CharField(max_length=25 , blank=False, default='')