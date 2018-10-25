from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib.auth import get_user_model
# Create your views here.

from .models import UserProfile


Users = get_user_model()

class UserProfileDetail(generic.DetailView):
	template_name = "accounts/user_profile.html"
	queryset = Users.objects.all()


	def get_object(self):
		return get_object_or_404(Users, username__iexact=self.kwargs.get("username"))



class UserFollowView(View):
	def get(self, request, username, *args, **kwargs):
		toggle_user = get_object_or_404(Users, username__iexact=username)
		if request.user.is_authenticated:
			user_profile, created = UserProfile.objects.get_or_create(user=request.user)
			if toggle_user in user_profile.following.all():
				user_profile.following.remove(toggle_user)
			else:
				user_profile.following.add(toggle_user)
		return redirect("user_profiles:user_profile", username=username)