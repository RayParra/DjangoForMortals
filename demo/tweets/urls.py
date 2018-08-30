from django.urls import path

from tweets import views


urlpatterns = [
	path('list_tweet/', views.list_tweet, name="list_tweet_view"),
	path('detail_tweet/<int:id>/', views.detail_tweet, name="detail_tweet_view"),
]