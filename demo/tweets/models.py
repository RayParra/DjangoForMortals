from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
# Create your models here.

from .validators import validate_content


class Tweet(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
	content = models.CharField(max_length=256, validators=[validate_content])
	update = models.DateTimeField(auto_now_add=True)
	timestamp = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return str(self.content)