from django.contrib import admin

from recommendation.models import Recommendation


class RecommendationAdmin(admin.ModelAdmin):
    list_display = ("id", "created_date", "recommended_email", "has_accepted")


admin.site.register(Recommendation, RecommendationAdmin)
