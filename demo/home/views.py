from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q

from django.views import generic
from tweets.models import Tweet
from tweets.forms import FormTweet
# Create your views here.


def index(request):
	return render(request, "home/index.html")


class Index(generic.ListView):
	template_name = "home/index.html"
	queryset = Tweet.objects.all()


	def get_queryset(self, *args, **kwargs):
		qs = Tweet.objects.all()
		print(self.request.GET)
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(Q(user__username__icontains=query) | Q(content__icontains=query))
		return qs

	def get_context_data(self, *args, **kwargs):
		context = super(Index, self).get_context_data(*args, **kwargs)
		context["create_form"] = FormTweet()
		context["create_url"] = reverse_lazy("index_view")
		return context