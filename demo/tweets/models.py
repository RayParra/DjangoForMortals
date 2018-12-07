import re
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils import timezone
# Create your models here.

from .validators import validate_content


class TweetManager(models.Manager):
	def retweet(self, user, parent_obj):
		if parent_obj.parent:
			og_parent = parent_obj.parent
		else:
			og_parent = parent_obj

		qs = self.get_queryset().filter(
			user=user,
			parent=parent_obj
			).filter(
				timestamp__year=timezone.now().year,
				timestamp__month=timezone.now().month,
				timestamp__day=timezone.now().day
			)
		if qs.exists():
			return None	

		obj = self.model (
			parent = og_parent,
			user = user,
			content = parent_obj.content,
			)
		obj.save()
		return obj



class Tweet(models.Model):
	parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
	content = models.CharField(max_length=256, validators=[validate_content])
	update = models.DateTimeField(auto_now_add=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	objects = TweetManager()


	def get_absolute_url(self):
		return reverse("tweets:Detail_Tweet_view", kwargs={"pk":self.pk})

	class Meta:
		ordering = ["-timestamp"]

	def __str__(self):
		return str(self.content)





def tweet_save_receiver(sender, instance, created, *args, **kwargs):
	if created and not instance.parent:
		print("some")
		user_regex = r'@(?P<username>[\w.@+-]+)'#r'@<str:username>' #
		m = re.match(user_regex, instance.content)
		#username = m.group("username")
		print(instance.content)
		print(username)
	
		# hash_regex = r'#<str:hashtag>'
		# m = re.search(hash_regex, instance.content)
		# hashtag = m.group("hashtag")
		# print(hashtag)

post_save.connect(tweet_save_receiver, sender=Tweet)








