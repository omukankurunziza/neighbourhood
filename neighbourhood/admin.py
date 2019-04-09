from django.contrib import admin

from .models import Admin,Profile,Neighbourhood,Business,User

# Register your models here.

admin.site.register(Admin)
admin.site.register(Profile)
admin.site.register(Neighbourhood)
admin.site.register(Business)
