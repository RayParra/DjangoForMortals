from django.urls import path

from accounts import views

app_name = "user_profiles"


urlpatterns = [
	path('user_profile/<str:username>/', views.UserProfileDetail.as_view(), name="user_profile"),
	path('user_profile/<str:username>/follow', views.UserFollowView.as_view(), name="followView"),	
]