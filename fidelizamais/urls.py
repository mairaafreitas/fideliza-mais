from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from referral.views import (ReferralViewSet, accept_referral, create_referral,
                            get_referrals, referral_detail)
from user.views import UserViewSet, get_users, user_detail

router = DefaultRouter()

router.register(r"referral", ReferralViewSet)
router.register(r"user", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("users/", get_users),
    path("user/<int:pk>", user_detail),
    path("referrals/", get_referrals),
    path("referral/<int:pk>", referral_detail),
    path("create-referral/", create_referral, name="create_referral"),
    path("accept-referral/", accept_referral, name="accept_referral"),
    path("admin/", admin.site.urls),
]
