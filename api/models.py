from django.db import models
from accounts.models import Profile

class Post(models.Model):
	user = models.ForeignKey(Profile, blank=False, on_delete=models.CASCADE, related_name='full_name')
	title = models.CharField(max_length=100, blank=True, default='')
	body = models.TextField(blank=True, default='')
    
	def __str__(self):
		return self.title