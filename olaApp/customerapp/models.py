from django.db import models
import datetime

# Create your models here.
class Customer(models.Model):
	customer_id = models.CharField(max_length = 200, unique=True, db_index=True)
	name = models.CharField(max_length = 200, null=True, blank=True)
	email = models.CharField(max_length = 100, null=True, blank=True)

	def __unicode__(self):
		return self.customer_id