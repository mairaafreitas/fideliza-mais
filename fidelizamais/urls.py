from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recommendation.views import RecommendationViewSet
from user.views import UserViewSet

router = DefaultRouter()

router.register(r"recommendation", RecommendationViewSet)
router.register(r"user", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
]
