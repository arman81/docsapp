
from django.db import models

# Create your models here.
from driverapp.models import Driver
from customerapp.models import Customer
from datetime import timezone
#dt.replace(tzinfo=timezone.utc)
# Create your models here.
REQUEST_CHOICES = (
	('wating','wating'),
	('ongoing','ongoing'),
	('completed','completed')
	)

class Request(models.Model):
	customer = models.ForeignKey(Customer,on_delete=models.SET_DEFAULT,default=None,blank=True,null=True)
	start_time = models.DateTimeField(null=True)
	end_time = models.DateTimeField(null=True)
	status = models.CharField(choices = REQUEST_CHOICES,max_length = 50,blank=True)
	driver = models.ForeignKey(Driver,on_delete=models.SET_DEFAULT,default=None,blank=True,null=True)
	active = models.BooleanField(default = True)

class CompleteRequest(models.Model):
	driver = models.ForeignKey(Driver,on_delete=models.SET_DEFAULT,default=None,blank=True,null=True)
	request = models.ForeignKey(Request,on_delete=models.SET_DEFAULT,default=None,blank=True,null=True)