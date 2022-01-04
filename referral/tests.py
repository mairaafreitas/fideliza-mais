import json

import django
from django.test import Client, TestCase
from django.urls import reverse

from referral.models import Referral
from user.models import User


class CreateReferralTests(TestCase):
    client = Client()
    user = None

    @classmethod
    def setUpClass(cls):
        super(CreateReferralTests, cls).setUpClass()
        django.setup()
        cls.user = User.objects.create(
            name="Marina",
            document="67576298014",  # 4devs
            email="marina@gmail.com",
            birth_date="2001-10-10",
            phone="10675432678",
        )

    def test_create_referral_success(self):
        valid_payload = {"user": self.user.id, "referred_email": "some_email@email.com"}

        response = self.client.post(
            reverse("create_referral"),
            data=json.dumps(valid_payload),
            content_type="application/json",
        )

        assert response.status_code == 201
        assert '"has_accepted":false' in str(response.content)
        assert '"referred_email":"some_email@email.com"' in str(response.content)
        assert '"user":1' in str(response.content)

    def teste_create_referral_invalid_data(self):
        invalid_payload = {"user": str(self.user.id), "referred_email": "some_email"}

        response = self.client.post(
            reverse("create_referral"),
            data=json.dumps(invalid_payload),
            content_type="application/json",
        )

        decode_response = response.content.decode("utf-8")
        assert response.status_code == 400
        assert "Erro ao criar uma indicação" in decode_response

    def test_create_referral_already_exist(self):
        Referral.objects.create(user=self.user, referred_email="fake_email@email.com")
        referral_already_exist_payload = {
            "user": self.user.id,
            "referred_email": "fake_email@email.com",
        }

        response = self.client.post(
            reverse("create_referral"),
            data=json.dumps(referral_already_exist_payload),
            content_type="application/json",
        )

        decode_response = response.content.decode("utf-8")
        assert response.status_code == 400
        assert "Não é possível indicar esse usuário novamente" in decode_response

    def test_create_referral_has_accepted(self):
        Referral.objects.create(
            user=self.user, referred_email="fake_email@email.com", has_accepted=True
        )
        referral_has_accepted_payload = {
            "user": self.user.id,
            "referred_email": "fake_email@email.com",
        }

        response = self.client.post(
            reverse("create_referral"),
            data=json.dumps(referral_has_accepted_payload),
            content_type="application/json",
        )

        decode_response = response.content.decode("utf-8")
        assert response.status_code == 400
        assert "Não é possível indicar esse usuário novamente" in decode_response

    def test_create_referral_self(self):
        referral_self = {"user": self.user.id, "referred_email": self.user.email}

        response = self.client.post(
            reverse("create_referral"),
            data=json.dumps(referral_self),
            content_type="application/json",
        )

        decode_response = response.content.decode("utf-8")
        assert response.status_code == 400
        assert "Não é possível indicar você mesmo" in decode_response
