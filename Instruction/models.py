from django.db import models

class conversation(models.Model):
    user = models.CharField(max_length=20)
    essay = models.CharField(max_length=10000,blank=True)
    response = models.CharField(max_length=10000,blank=True)
    problem = models.CharField(max_length=25,blank=True)

# Create your models here.
