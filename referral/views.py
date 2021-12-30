from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from referral.email.send_email import send_email
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


@api_view(["POST"])
def create_referral(request):
    serializer = ReferralSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            "Erro ao criar uma indicação", status=status.HTTP_400_BAD_REQUEST
        )

    referral = Referral.objects.filter(
        referred_email=serializer.validated_data["referred_email"]
    ).first()

    if referral and (referral.is_active() or referral.has_accepted):
        return Response(
            "Não é possível indicar esse usuário novamente",
            status=status.HTTP_400_BAD_REQUEST,
        )

    serializer.save()

    referral_id = serializer.data["id"]
    url = f"www.fidelizamais.com.br/refer-a-friend/{referral_id}"

    referral_email = serializer.data["referred_email"]
    send_email(referral_email, url)

    return Response(serializer.data, status=status.HTTP_201_CREATED)
