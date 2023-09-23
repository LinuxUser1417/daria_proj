from django.contrib import admin
from .models import User, CustomUser, CustomUserManager

admin.site.register([User, CustomUser])