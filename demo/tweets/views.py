from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.db.models import Q
from django.urls import reverse_lazy

from tweets.models import Tweet
from tweets.forms import FormTweet
from .mixins import FormsUserNeededMixin
# Create your views here.


class ReTweetView(View):
	def get(self, request, pk, *args, **kwargs):
		tweet = get_object_or_404(pk=pk)
		if request.user.is_authenticated():
			new_tweet = Tweet.objects.retweet(request.user, tweet)
			return HttpResponseRedirect(new_tweet.get_absolute_url())
		return HttpResponseRedirect(tweet.get_absolute_url())

# CRUD

#Create
class Create_Tweet(FormsUserNeededMixin, generic.CreateView):
	template_name = "tweets/create_tweet.html"
	model = Tweet
	form_class = FormTweet
	#fields = ["content"]
	success_url = "/"

	def get_context_data(self, *args, **kwargs):
		context = super(Create_Tweet, self).get_context_data(*args, **kwargs)
		context["create_form"] = FormTweet()
		#context["create_url"] = reverse_lazy("List_Tweet_view")
		return context




def create_tweet(request):
	form = FormTweet(request.POST or None)
	if request.user.is_authenticated:
		error_message = "User is Logged"
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user

			instance.save()
	else:
		error_message = "User Must Be Logged"
		#form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User Must Be Logged"])
	context = {
		"form": form,
		"error_message": error_message
	}
	return render(request, "tweets/create_tweet.html", context)

#Retrieve#Detail
class Detail_Tweet(generic.DetailView):
	template_name = "tweets/detail_tweet.html"
	model = Tweet


	#def get_object(self):
	#	return Tweet.objects.get(pk=id)

# def detail_tweet(request, id=1):
# 	tweet = Tweet.objects.get(id=id)
# 	context = {
# 		"tweet": tweet
# 	}
# 	return render(request, "tweets/detail_tweet.html", context)


#Update
class Update_Tweet(generic.UpdateView):
	template_name = "tweets/update_tweet.html"
	model = Tweet
	fields = ["content"]
	success_url = "/tweet/list_tweet/"

#Delete
class Delete_Tweet(generic.DeleteView):
	template_name = "tweets/delete_tweet.html"
	model = Tweet
	success_url = "/tweet/list_tweet/"

#List
class List_Tweet(generic.ListView):
	template_name = "tweets/list_tweet.html"
	queryset = Tweet.objects.all()

	def get_queryset(self, *args, **kwargs):
		qs = Tweet.objects.all()
		print(self.request.GET)
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(Q(user__username__icontains=query) | Q(content__icontains=query))
		return qs
		
	def get_context_data(self, *args, **kwargs):
		context = super(List_Tweet, self).get_context_data(*args, **kwargs)
		context["create_form"] = FormTweet()
		context["create_url"] = reverse_lazy("tweets:Create_Tweet_view")
		return context

#def list_tweet(request):
#	queryset = Tweet.objects.all()
#	return render(request, "tweets/list_tweet.html", {"tweet": queryset})

