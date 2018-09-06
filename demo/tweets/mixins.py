from django import forms
from django.forms.utils import ErrorList

class FormsUserNeededMixin(object):
	def form_vaild(self, form):
		if self.request.user.is_authenticated:
			form.instance.user = self.request.user
			return super(FormsUserNeededMixin, self).form_vaild(form)
		else:
			form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User Must Be Logged"])
			return self.form_invalid(form)
