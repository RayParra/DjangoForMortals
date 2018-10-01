from django.urls import path
from django.views.generic.base import RedirectView
from tweets import views

app_name = 'tweets'

urlpatterns = [
	path('',RedirectView.as_view(url="/")),
	path('search', views.List_Tweet.as_view(), name="List_Tweet_view"),
	path('detail_tweet/<int:pk>/', views.Detail_Tweet.as_view(), name="Detail_Tweet_view"),
	path('update_tweet/<int:pk>/', views.Update_Tweet.as_view(), name="Update_Tweet_view"),
	path('create_tweet/', views.Create_Tweet.as_view(), name="Create_Tweet_view"),
	path('delete_tweet/<int:pk>/', views.Delete_Tweet.as_view(), name="Delete_Tweet_view"),


	path('create_tweet2/', views.create_tweet, name="Create_Tweet_view2"),
]