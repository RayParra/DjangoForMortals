from django.shortcuts import render

from tweets.models import Tweet
# Create your views here.


# CRUD

#Create


#Retrieve


#Update


#Delete


#List
def list_tweet(request):
	queryset = Tweet.objects.all()
	return render(request, "tweets/list_tweet.html", {"tweet": queryset})

#Detail

