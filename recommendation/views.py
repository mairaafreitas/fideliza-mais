from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from recommendation.models import Recommendation
from recommendation.serializers import RecommendationSerializer


class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer


@api_view(["GET"])
def get_recommendations(request):
    recommendation = Recommendation.objects.all()
    serializer = RecommendationSerializer(recommendation, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def recommendation_detail(request, pk):
    recommendation = get_object_or_404(Recommendation, pk=pk)
    serializer = RecommendationSerializer(recommendation)
    return Response(serializer.data)
