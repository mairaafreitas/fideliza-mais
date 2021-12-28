from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from referral.models import Referral
from referral.serializers import ReferralSerializer


class ReferralViewSet(viewsets.ModelViewSet):
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer


@api_view(["GET"])
def get_referrals(request):
    referral = Referral.objects.all()
    serializer = ReferralSerializer(referral, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def referral_detail(request, pk):
    referral = get_object_or_404(Referral, pk=pk)
    serializer = ReferralSerializer(referral)
    return Response(serializer.data)
