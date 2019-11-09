from django.contrib import admin
from .models import Seller, Property, Address, Image, Contact, Message

# Register your models here.

class SellerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Seller, SellerAdmin)

class PropertyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Property, PropertyAdmin)

class AddressAdmin(admin.ModelAdmin):
    pass


admin.site.register(Address, AddressAdmin)

class ImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Image, ImageAdmin)


class ContactAdmin(admin.ModelAdmin):
    pass


admin.site.register(Contact, ContactAdmin)

class MessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Message, MessageAdmin)