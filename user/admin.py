from django.contrib import admin

from user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "document", "name", "birth_date", "phone", "balance")


admin.site.register(User, UserAdmin)
