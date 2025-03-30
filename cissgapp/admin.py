from django.contrib import admin
from .models import extenduser, academic

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Register your models here.

admin.site.register(extenduser)
admin.site.register(academic)
# admin.site.register(CustomUser)