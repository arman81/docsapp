from django.db import models

# Create your models here.

class Driver(models.Model):
	name = models.CharField(max_length = 200,blank=True,null=True)
	location = models.CharField(max_length = 200,blank=True,null=True)

