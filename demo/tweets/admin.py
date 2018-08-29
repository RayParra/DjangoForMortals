from django.contrib import admin

# Register your models here.
from .models import Tweet


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
	list_display = ["id", "content"]
	list_display_links = ('content',)
