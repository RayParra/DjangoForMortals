from django.test import TestCase

from django.contrib.auth import get_user_model

# Create your tests here.


from .models import UserProfile


User = get_user_model()


class UserProfileTestCase(TestCase):
	def setUp(self):
		self.username = "some_user"
		new_user = User.objects.create(username=self.username)


	def test_profile_created(self):
		username = self.username
		user_profile = UserProfile.objects.filter(user__username=self.username)
		print(user_profile)
		self.assertTrue(user_profile.exists())
		self.assertTrue(user_profile.count()==1)






