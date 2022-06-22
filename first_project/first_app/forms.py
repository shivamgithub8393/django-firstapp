from django import forms
from django.core import validators
from first_app.models import User

class FormName(forms.Form):
	name = forms.CharField(validators=[
			validators.MaxLengthValidator(20)])
	email = forms.EmailField()
	text = forms.CharField(widget=forms.Textarea)
	# add a input which is hidden by default to catch bot
	botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[
			validators.MaxLengthValidator(2)])
		

class NewUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = '__all__'
