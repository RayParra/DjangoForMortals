from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth import get_user_model
# Create your views here.


Users = get_user_model()

class UserProfileDetail(generic.DetailView):
	template_name = "accounts/user_profile.html"
	queryset = Users.objects.all()


	def get_object(self):
		return get_object_or_404(Users, username__iexact=self.kwargs.get("username"))
