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


	def get_context_data(self, *args, **kwargs):
		context = super(UserProfileDetail, self).get_context_data(*args, **kwargs)
		context["following"] = UserProfile.objects.is_following(self.request.user, self.get_object())
		return context


class UserFollowView(View):
	def get(self, request, username, *args, **kwargs):
		toggle_user = get_object_or_404(Users, username__iexact=username)
		if request.user.is_authenticated:
			is_following = UserProfile.objects.toggle_follow(request.user, toggle_user)
		return redirect("user_profiles:user_profile", username=username)