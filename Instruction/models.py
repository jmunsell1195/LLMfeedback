from django.db import models

class conversation(models.Model):
    user = models.CharField(max_length=20)
    prompt = models.CharField(max_length=10000,blank=True)
    response = models.CharField(max_length=5000,blank=True)

# Create your models here.
