from django.db import models

# Create your models here.
class Information(models.Model):
    Picture = models.ImageField(null = True, blank = True, upload_to = "images/")
    Name = models.CharField(max_length=30)
    Age = models.IntegerField(blank=True, null=True)
    Email = models.EmailField(blank=True, null=True)
    Address = models.CharField(max_length=250, blank=True,null=True)
    Contact = models.IntegerField(blank=True, null=True)
    Description = models.TextField(max_length = 2000)

class Education(models.Model):
    Year = models.DateField(blank=True, null=True)
    Level = models.CharField(max_length=250)
    School = models.CharField(max_length=500, null=True, blank=False)
