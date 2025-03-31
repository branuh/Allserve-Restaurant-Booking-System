from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(CustomUser)
class CustomUser(UserAdmin):
    #model to map to
    list_display = ("username", "email", "is_staff", "is_active", "date_joined")
    list_filter = ("is_staff", "is_active")
    #search filter
    search_fields = ("username",)


#create superuser
#py manage.py createsuperuser