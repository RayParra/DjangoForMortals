from django.shortcuts import render


from django.views import generic
from tweets.models import Tweet

# Create your views here.


def index(request):
	return render(request, "home/index.html")


class Index(generic.ListView):
	template_name = "home/index.html"
	queryset = Tweet.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(Index, self).get_context_data(*args, **kwargs)
		return context