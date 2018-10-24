from django.db import models
from django.conf import settings
# Create your models here.



class UserProfileManager(models.Manager):
	use_for_related_fields = True
	def all(self):
		#print(dir(self))
		qs = self.get_queryset().all()
		print(self.instance)
		if self.instance:
				qs = qs.exclude(user=self.instance)

		return qs


class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
	following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by') 

	objects = UserProfileManager()

	def __str__(self):
		return str(self.following.all().count())


	def get_following(self):
		users = self.following.all()
		return users.exclude(username=self.user)