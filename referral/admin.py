from django.contrib import admin

from referral.models import Referral


class ReferralAdmin(admin.ModelAdmin):
    list_display = ("id", "created_date", "referred_email", "has_accepted")


admin.site.register(Referral, ReferralAdmin)
