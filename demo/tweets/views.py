from django.shortcuts import render
from django.views import generic
from django.forms.utils import ErrorList
from django import forms

from tweets.models import Tweet
from tweets.forms import FormTweet
# Create your views here.


# CRUD

#Create
class Create_Tweet(generic.CreateView):
	template_name = "tweets/create_tweet.html"
	model = Tweet
	fields = ["content"]
	success_url = "/tweet/list_tweet/"


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

	def get_context_data(self, *args, **kwargs):
		context = super(List_Tweet, self).get_context_data(*args, **kwargs)
		return context

#def list_tweet(request):
#	queryset = Tweet.objects.all()
#	return render(request, "tweets/list_tweet.html", {"tweet": queryset})

