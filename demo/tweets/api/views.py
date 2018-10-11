from rest_framework import generics
from rest_framework import permissions
from django.db.models import Q

from tweets.models import Tweet
from .serializers import TweetModelSerializer


class TweetCreateAPIView(generics.CreateAPIView):
	serializer_class = TweetModelSerializer
	#permission_classes = [permissions.IsAuthenticated]


	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

		

class TweetListAPIView(generics.ListAPIView):
	serializer_class = TweetModelSerializer

	def get_queryset(self, *args, **kwargs):
		qs = Tweet.objects.all()
		print(self.request.GET)
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(Q(user__username__icontains=query) | Q(content__icontains=query))
		return qs