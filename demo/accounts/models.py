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


	def toggle_follow(self, user, to_toggle_user):
		user_profile, created = UserProfile.objects.get_or_create(user=user)
		if to_toggle_user in user_profile.following.all():
			user_profile.following.remove(to_toggle_user)
			added = True
		else:
			user_profile.following.add(to_toggle_user)
			added = False
		return added


	def is_following(self, user, followed_by_user):
		user_profile, created = UserProfile.objects.get_or_create(user=user)
		if created:
			return False
		else:
			if followed_by_user in user_profile.following.all():
				return True
		return False


class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
	following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by') 

	objects = UserProfileManager()

	def __str__(self):
		return str(self.following.all().count())


	def get_following(self):
		users = self.following.all()
		return users.exclude(username=self.user)