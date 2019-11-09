from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Seller(models.Model):

    GENDER_CHOICES = (('m','Male'), ('f', 'Female'))
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4)
    national_id = models.IntegerField()
    dob = models.DateField()
    image = models.ImageField(upload_to = 'images/', null=True)
    gender = models.CharField(choices = GENDER_CHOICES, max_length = 1)
    user = models.OneToOneField(User, related_name = 'seller', on_delete = models.CASCADE)
    address = models.ForeignKey('Address', related_name='seller', on_delete = models.CASCADE)

class Property(models.Model):

    CATEGORY_CHOICES = (('b', 'Buy'), ('r', 'Rent'), ('m', 'Mortgage'))
    HOUSE_TYPE_CHOICES = (('a', 'Appartment'), ('v', 'Vella'))
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4)
    title = models.CharField(max_length = 200)
    house_type = models.CharField(choices = HOUSE_TYPE_CHOICES, max_length = 1)
    lot = models.IntegerField()
    year_built = models.IntegerField()
    category = models.CharField(choices = CATEGORY_CHOICES, max_length = 1)
    description = models.TextField()
    address = models.ForeignKey('Address', on_delete = models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete = models.CASCADE)

class Address(models.Model):
    
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    street_no = models.IntegerField()
    phone_no1 = models.CharField(max_length=20)
    phone_no2 = models.CharField(max_length=20, null=True)


class Image(models.Model):

    uid = models.UUIDField(primary_key = True, default = uuid.uuid4)
    Property_img = models.ImageField(upload_to = 'images/', null = True)
    Property = models.ForeignKey(Property, on_delete = models.CASCADE)



class Contact(models.Model):

    uid = models.UUIDField(primary_key = True, default = uuid.uuid4)
    user_id = models.OneToOneField(User, on_delete = models.SET_NULL, null=True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length=200)
    address = models.ForeignKey(Address, on_delete = models.CASCADE)
    


class Message(models.Model):

    uid = models.UUIDField(primary_key = True, default = uuid.uuid4)
    sender = models.ForeignKey(Contact, related_name='sender', on_delete = models.SET_NULL, null=True)
    reciever = models.ForeignKey(Contact, related_name='receiver', on_delete = models.SET_NULL, null=True) 
    Property = models.ForeignKey(Property, on_delete = models.CASCADE)
    subject = models.TextField()
    message = models.TextField()





