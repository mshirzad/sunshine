from django import forms
from django.forms.widgets import TextInput, PasswordInput

class SigninForm(forms.Form): #SigninForm	
	username = forms.CharField(required=False, widget=TextInput())
	password = forms.CharField(required=False, widget=PasswordInput())

class SignupForm(forms.Form):	# SignupForm
	first_name = forms.CharField(required=True, widget=TextInput())
	last_name = forms.CharField(required=True, widget=TextInput())
	email = forms.CharField(required=True, widget=TextInput())
	username = forms.CharField(required=True, widget=TextInput())
	password = forms.CharField(required=True, widget=PasswordInput())
	confirm_password = forms.CharField(required=True, widget=PasswordInput())

class ProfileForm(SignupForm): # ProfileForm
	GENDER_CHOICES = (('m','Male'), ('f', 'Female'))
	username = None
	password = None
	confirm_password = None
	national_id = forms.CharField(required=True, widget=TextInput())
	dob = forms.DateField(required=True)
	gender = forms.ChoiceField(required=True, choices=GENDER_CHOICES)
	image = forms.ImageField(required=False)
	country = forms.CharField(required=True)
	city = forms.CharField(required=True)
	district = forms.CharField(required=True, widget=TextInput())
	area = forms.CharField(required=True, widget=TextInput())
	street_no = forms.IntegerField(required=True, widget=TextInput())
	phone_no1 = forms.CharField(required=True, widget=TextInput())
	phone_no2 = forms.CharField(required=False, widget=TextInput())


class ChangePasswordForm(forms.Form):
	current_password = forms.CharField(required=True, widget=PasswordInput())
	new_password = forms.CharField(required=True, widget=PasswordInput())
	confirm_password = forms.CharField(required=True, widget=PasswordInput())


class PropertyForm(forms.Form):
	CATEGORY_CHOICES = (('b', 'Buy'), ('r', 'Rent'), ('m', 'Mortgage'))
	HOUSE_TYPE_CHOICES = (('a', 'Appartment'), ('v', 'Vella'))
	title = forms.CharField(required=True, widget=TextInput())
	house_type = forms.ChoiceField(required=True, choices=HOUSE_TYPE_CHOICES)
	lot = forms.IntegerField(required=False, widget=TextInput())
	year_built = forms.IntegerField(required=False, widget=TextInput())
	category = forms.ChoiceField(required=True, choices=CATEGORY_CHOICES)
	description = forms.Textarea()
