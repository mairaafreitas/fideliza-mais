from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from referral.email.send_email import send_email
from referral.models import Referral
from referral.serializers import ReferralSerializer
from user.models import User
from user.serializers import UserSerializer


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

    user = User.objects.filter(name=serializer.validated_data["user"]).first()
    user_indicated_email = serializer.validated_data["referred_email"]

    if user.email == user_indicated_email:
        return Response(
            "Não é possível indicar você mesmo",
            status=status.HTTP_400_BAD_REQUEST,
        )

    serializer.save()

    referral_id = serializer.data["id"]
    url = f"www.fidelizamais.com.br/refer-a-friend/{referral_id}"

    referral_email = serializer.data["referred_email"]
    send_email(referral_email, url)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def accept_referral(request):
    referral = Referral.objects.get(
        referred_email=request.data.get("referred_email")
    )  # noqa
    name = request.data.get("name")
    document = request.data.get("document")
    birth_date = request.data.get("birth_date")
    phone = request.data.get("phone")

    if not referral.is_active() or referral.has_accepted:
        return Response(
            "Essa indicação já foi aceita ou não está mais ativa",
            status=status.HTTP_400_BAD_REQUEST,
        )

    accepted_serializar = UserSerializer(
        data={
            "name": name,
            "document": document,
            "email": referral.referred_email,
            "birth_date": birth_date,
            "phone": phone,
        }
    )
    if not accepted_serializar.is_valid():
        return Response(
            "Erro ao aceitar a indicação", status=status.HTTP_400_BAD_REQUEST
        )

    referral.has_accepted = True
    referral.user.balance += 10

    accepted_serializar.save()
    referral.user.save()
    referral.save()

    response = {
        "email": referral.referred_email,
        "name": name,
        "document": document,
        "phone": phone,
        "birth_date": birth_date,
    }

    return Response(response, status=status.HTTP_201_CREATED)
