from django.urls import path
from home import views
from tweets.views import Detail_Tweet

urlpatterns = [
   path('', views.Index.as_view(), name="index_view"),
   path('detail_tweet/<int:pk>/', Detail_Tweet.as_view(), name="Detail_Tweet_view"),
]
