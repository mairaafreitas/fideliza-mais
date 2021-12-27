from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recommendation.views import (RecommendationViewSet, get_recommendations,
                                  recommendation_detail)
from user.views import UserViewSet, get_users, user_detail

router = DefaultRouter()

router.register(r"recommendation", RecommendationViewSet)
router.register(r"user", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("users/", get_users),
    path("user/<int:pk>", user_detail),
    path("recommendations/", get_recommendations),
    path("recommendation/<int:pk>", recommendation_detail),
    path("admin/", admin.site.urls),
]
