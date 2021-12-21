from rest_framework import serializers

from recommendation.models import Recommendation


class RecommendationSerializer(serializers.ModelSerializer):
    created_date = serializers.ReadOnlyField()
    has_accepted = serializers.ReadOnlyField()

    class Meta:
        model = Recommendation
        fields = ["user", "recommended_email", "created_date", "has_accepted"]
