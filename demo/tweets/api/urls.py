from django.urls import path
from django.views.generic.base import RedirectView
from tweets.api import views

app_name = 'tweet-api'

urlpatterns = [
	
	path('', views.TweetListAPIView.as_view(), name="TweetListAPIView_api"),
	path('detail_tweet/<int:pk>/retweet', views.RetweetAPIView.as_view(), name="RetweetAPIView"),
	# path('detail_tweet/<int:pk>/', views.Detail_Tweet.as_view(), name="Detail_Tweet_view"),
	# path('update_tweet/<int:pk>/', views.Update_Tweet.as_view(), name="Update_Tweet_view"),
	path('create/', views.TweetCreateAPIView.as_view(), name="create"),
	# path('delete_tweet/<int:pk>/', views.Delete_Tweet.as_view(), name="Delete_Tweet_view"),


	# path('create_tweet2/', views.create_tweet, name="Create_Tweet_view2"),
]