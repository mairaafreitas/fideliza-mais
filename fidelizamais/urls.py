from django.contrib import admin
from django.urls import path

from referral.views import (accept_referral, create_referral, get_referrals,
                            referral_detail)
from user.views import get_users, user_detail

urlpatterns = [
    path("users/", get_users),
    path("user/<int:pk>", user_detail),
    path("referrals/", get_referrals),
    path("referral/<int:pk>", referral_detail),
    path("create-referral/", create_referral, name="create_referral"),
    path("accept-referral/", accept_referral, name="accept_referral"),
    path("admin/", admin.site.urls),
]
