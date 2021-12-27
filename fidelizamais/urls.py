from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recommendation.views import RecommendationViewSet
from user.views import UserViewSet, get_users

router = DefaultRouter()

router.register(r"recommendation", RecommendationViewSet)
router.register(r"user", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("users/", get_users),
    path("admin/", admin.site.urls),
]
