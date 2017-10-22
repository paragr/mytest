from django import forms
from .models import AccessRequests

class AccessRequestForm(forms.ModelForm):
	users_list = forms.CharField(widget=forms.Textarea)
	env = forms.CharField()
	
	class Meta:
		model = AccessRequests
		fields = ('users_list','env')
