from django import forms


from .models import Tweet


class FormTweet(forms.ModelForm):
	class Meta:
		model = Tweet

		fields = ["content"]