from django.contrib import admin
from .models import Discussion, Comment, Category, Like, DisLike
# Register your models here.

admin.site.register([Discussion, Comment, Category, Like, DisLike])