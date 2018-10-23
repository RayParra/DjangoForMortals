from django.db import models
from django.conf import settings
# Create your models here.





class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
	following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by') 


	def __str__(self):
		return str(self.following.all().count())