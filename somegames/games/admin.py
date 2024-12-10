from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

# Register your models here.

admin.site.unregister(Group)
admin.site.unregister(User)

class ProfileInUser(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = [
        "username",
        "password"
    ]
    inlines = [ProfileInUser]

admin.site.register(User, UserAdmin)