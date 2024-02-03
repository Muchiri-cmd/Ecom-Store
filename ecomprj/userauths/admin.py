from django.contrib import admin
from django.db import models
from userauths.models import User,Profile

#Display table
class UserAdmin(admin.ModelAdmin):
    list_display=['username','email','bio']
class ProfileAdmin(admin.ModelAdmin):
    list_display=['full_name','bio','phone']
# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Profile,ProfileAdmin)