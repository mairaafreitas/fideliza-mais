from rest_framework import viewsets

from recommendation.models import Recommendation
from recommendation.serializers import RecommendationSerializer


class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
