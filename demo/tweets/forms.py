from django import forms


from .models import Tweet


class FormTweet(forms.ModelForm):

	#content = forms.CharField(label="" ,widget=forms.Textarea(attrs={"placeholder": "Your Message", "class": "form-control"}))

	class Meta:
		model = Tweet

		fields = ["content"]