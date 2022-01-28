#User Admin Classes
#Django
from re import search
from django.contrib import admin

#Models #API
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','first_name', 'last_name', 'email')




