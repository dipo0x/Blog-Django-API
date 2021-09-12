from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, blank=False, on_delete=models.CASCADE,related_name='profiles')
	name = models.CharField(max_length=100, blank=True, default='')
	age = models.IntegerField(blank=True, default='')
	address = models.CharField(max_length=100, blank=True, default='Your kaba')

	def __str__(self):
	    return self.name