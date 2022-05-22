from django.contrib import admin
from .models import UserInfo


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth', 'phone', 'school', 'company', 'profession', 'address', 'about_me')
    list_filter = ('phone', 'school', 'company', 'profession')


admin.site.register(UserInfo, UserInfoAdmin)

# Register your models here.
