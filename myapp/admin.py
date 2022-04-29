from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):    
    model = User
    list_display = ['username']

# register models to Django admin
admin.site.register(Location)
admin.site.register(Park)
admin.site.register(Breed)
admin.site.register(Gender)
admin.site.register(Socialization)
admin.site.register(Aggression)
admin.site.register(Tag)
admin.site.register(Size)
admin.site.register(Dog)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Image)
admin.site.register(Connection)
admin.site.register(Conversation)
admin.site.register(Message)
admin.site.register(Comment)