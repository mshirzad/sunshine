from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import ProfileForm, SigninForm, SignupForm, ChangePasswordForm, PropertyForm
from django.db import IntegrityError
from .models import Seller, Address


# Create your views here.


def home(request):
	print(request.user)
	return render (request, 'index.html', context={'no_profile': True})



def profile_view(request):

	form = ProfileForm
	user = request.user
	has_profile = True

	try:
		seller = Seller.objects.get(user=user)
		address = seller.address
	except Seller.DoesNotExist:
		
		has_profile = False

	

	# print(seller.national_id)

	if request.method != 'POST':

		if has_profile == False:
			return render (request, 'profile.html', {'form': form,
				'info': {'first_name': user.first_name,
				'last_name': user.last_name,
				'email': user.email,
				'username': user.username,
				'password': user.password},
				'editable': True
				})
		else:
			try:
				editable = bool(request.GET.get('edit'))
			except:
				editable = False

			print(editable)

			return render (request, 'profile.html', {'form': form,
				'info': {'first_name': user.first_name,
				'last_name': user.last_name,
				'email': user.email,
				'username': user.username,
				'password': user.password,
				'national_id': seller.national_id,
				'gender': seller.gender,
				'dob': seller.dob,
				'image': seller.image,
				'country': address.country,
				'city': address.city,
				'district': address.district,
				'area': address.area,
				'street_no': address.street_no,
				'phone_no1': address.phone_no1,
				'phone_no2': address.phone_no2
				},
				'editable': editable
				})


	form = ProfileForm(request.POST)

	print(form)

	if form.is_valid():
		data = form.cleaned_data


		# request.user.username = data['username']
		request.user.first_name = data['first_name']

		request.user.save()

		address_defaults = {
			'country': data['country'],
			'city': data['city'],
			'district': data['district'],
			'area': data['area'],
			'street_no': data['street_no'],
			'phone_no1': data['phone_no1'], 
			'phone_no2': data['phone_no2']
		}

		address, created = Address.objects.update_or_create(seller__user=request.user, defaults=address_defaults)

		print('address ', created)
		seller_defaults = {
			'national_id': data['national_id'],
			'dob': data['dob'],
			'gender': data['gender'],
			'image': request.FILES.get('image'),
			'user' : request.user,
			'address' : address
		}

		seller, created = Seller.objects.update_or_create(user=request.user, defaults=seller_defaults)

		print('seller ', created)
		

		# address = Address(country=data['country'], city=data['city'], district=data['district'],\
		# 	area=data['area'], street_no=data['street_no'], phone_no1=data['phone_no1'], phone_no2=data['phone_no2'])

		# seller = Seller(national_id=data['national_id'], dob=data['dob'], gender=data['gender'], image=data['image'], user=user, address=address)

		# address.save()
		# seller.save()

		return HttpResponseRedirect('/')
	else:
		print('invalid form')
		


def signup_view(request):

	if request.method != 'POST':
		form = SignupForm
		return render (request, 'signup.html', {'form': form})

	# print(request.POST)
	form = SignupForm(request.POST)

	if form.is_valid():
		data = form.cleaned_data

		if data['password'] != data['confirm_password']:
			message = "Password didn't Match"
			return render (request, 'signup.html', {'form': form, 'failed': True, 'message': message})

		first_name = data['first_name']
		last_name = data['last_name']

		try:
			user = User.objects.create_user(data['username'], data['email'], data['password'], \
				first_name=first_name, last_name=last_name)	

		except Exception as e:
			# print(e)
			message = "Username already exists"
			return render (request,'signup.html', {'form': form, 'failed': True, 'message': message })

		user.save()
		login(request, user)

		return HttpResponseRedirect('/profile_view/')
    


def signin_view(request):
	if request.method != 'POST':
		if not request.user.is_authenticated:
			form = SigninForm()
			return render (request, 'signin.html', {'form': form})
		else:
			return HttpResponseRedirect('/profile_view/')

	form = SigninForm(request.POST)

	if form.is_valid():

		data = form.cleaned_data

		username = data['username']
		password = data['password']

		if not request.user.is_authenticated:

			user = authenticate(request, username = username, password = password)

			if user is not None:
				login(request, user)
				return HttpResponseRedirect('/profile_view/')
			else:
				return render (request,'signin.html', {'form': form, 'failed': True})

		else:
			print("User is authenticated")
			return HttpResponseRedirect('/profile_view/')



def change_password(request):

	if request.method == 'POST':
		form = ChangePasswordForm(request.POST)
		user = request.user

		if form.is_valid():

			data = form.cleaned_data

			current_password = data['current_password']
			new_password = data['new_password']
			confirm_password = data['confirm_password']

			if user.check_password(current_password):

				if confirm_password != new_password:
					message = "Password didn't Match"
					return render (request, 'profile.html', {'form': form, 'failed': True, 'message': message})

				else:
					message = "Password Changed"
					user.set_password(new_password)

					return render (request, 'profile.html', {'changed': True, 'message': message})

			else:
				message = "Incorrect Password"
				return render (request, 'profile.html', {'form': form, 'failed': True, 'message': message})



def sell_property(request):

	if request.method != 'POST':

		form = PropertyForm()
		return render (request, 'sell_property.html', {'form': form})




def logout_(request):
	logout(request)
	return HttpResponseRedirect('/signin_view/')