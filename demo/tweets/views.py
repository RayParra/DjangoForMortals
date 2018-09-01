from django.shortcuts import render
from django.views import generic

from tweets.models import Tweet
# Create your views here.


# CRUD

#Create


#Retrieve


#Update


#Delete


#List
class List_tweet(generic.ListView):
	template_name = "tweets/list_tweet.html"
	queryset = Tweet.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(List_tweet, self).get_context_data(*args, **kwargs)
		return context

#def list_tweet(request):
#	queryset = Tweet.objects.all()
#	return render(request, "tweets/list_tweet.html", {"tweet": queryset})

#Detail
def detail_tweet(request, id=1):
	tweet = Tweet.objects.get(id=id)
	context = {
		"tweet": tweet
	}
	return render(request, "tweets/detail_tweet.html", context)
