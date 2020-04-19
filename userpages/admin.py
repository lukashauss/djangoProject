from django.contrib import admin
from .models import UserData, Post, Blog

# Register your models here.
admin.site.register(UserData)
admin.site.register(Post)
admin.site.register(Blog)
