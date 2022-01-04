import json
from datetime import date
from unittest.mock import patch

import django
from django.test import Client, TestCase
from django.urls import reverse
from freezegun import freeze_time

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
        payload = {"user": self.user.id, "referred_email": "some_email@email.com"}

        response = self.client.post(
            reverse("create_referral"),
            data=json.dumps(payload),
            content_type="application/json",
        )

        assert response.status_code == 201
        assert '"has_accepted":false' in str(response.content)
        assert '"referred_email":"some_email@email.com"' in str(response.content)
        assert '"user":1' in str(response.content)

    def teste_create_referral_invalid_data(self):
        payload = {"user": str(self.user.id), "referred_email": "some_email"}

        response = self.client.post(
            reverse("create_referral"),
            data=json.dumps(payload),
            content_type="application/json",
        )

        decode_response = response.content.decode("utf-8")
        assert response.status_code == 400
        assert "Erro ao criar uma indicação" in decode_response

    def test_create_referral_already_exist(self):
        Referral.objects.create(user=self.user, referred_email="fake_email@email.com")
        payload = {
            "user": self.user.id,
            "referred_email": "fake_email@email.com",
        }

        response = self.client.post(
            reverse("create_referral"),
            data=json.dumps(payload),
            content_type="application/json",
        )

        decode_response = response.content.decode("utf-8")
        assert response.status_code == 400
        assert "Não é possível indicar esse usuário novamente" in decode_response

    def test_create_referral_has_accepted(self):
        Referral.objects.create(
            user=self.user, referred_email="fake_email@email.com", has_accepted=True
        )
        payload = {
            "user": self.user.id,
            "referred_email": "fake_email@email.com",
        }

        response = self.client.post(
            reverse("create_referral"),
            data=json.dumps(payload),
            content_type="application/json",
        )

        decode_response = response.content.decode("utf-8")
        assert response.status_code == 400
        assert "Não é possível indicar esse usuário novamente" in decode_response

    def test_create_referral_self(self):
        payload = {"user": self.user.id, "referred_email": self.user.email}

        response = self.client.post(
            reverse("create_referral"),
            data=json.dumps(payload),
            content_type="application/json",
        )

        decode_response = response.content.decode("utf-8")
        assert response.status_code == 400
        assert "Não é possível indicar você mesmo" in decode_response


class AcceptReferralTests(TestCase):
    client = Client()
    user = None
    referral = None

    @classmethod
    def setUpClass(cls):
        super(AcceptReferralTests, cls).setUpClass()
        django.setup()
        cls.user = User.objects.create(
            name="Larissa",
            document="61221481053",  # 4devs
            email="larissa@gmail.com",
            birth_date="2000-10-10",
            phone="12675432678",
        )
        cls.referral = Referral.objects.create(
            user=cls.user, referred_email="geovana@gmail.com"
        )

    def test_accept_referral_success(self):
        payload = {
            "referred_email": "geovana@gmail.com",
            "name": "Geovana",
            "document": "66556655074",
            "birth_date": "1998-10-10",
            "phone": "13675432678",
        }

        response = self.client.post(
            reverse("accept_referral"),
            data=json.dumps(payload),
            content_type="application/json",
        )

        assert response.status_code == 201
        assert '"email":"geovana@gmail.com"' in str(response.content)
        assert '"name":"Geovana"' in str(response.content)
        assert '"document":"66556655074"' in str(response.content)
        assert '"birth_date":"1998-10-10"' in str(response.content)
        assert '"phone":"13675432678"' in str(response.content)

    def test_accept_referral_invalid_data(self):
        payload = {
            "referred_email": "geovana@gmail.com",
            "name": "Geovana",
            "document": "01234567890",
            "birth_date": "1998-10-10",
            "phone": "1675432678",
        }

        response = self.client.post(
            reverse("accept_referral"),
            data=json.dumps(payload),
            content_type="application/json",
        )

        decode_response = response.content.decode("utf-8")
        assert response.status_code == 400
        assert "Erro ao aceitar a indicação" in decode_response

    def test_accept_referral_nonexistent(self):
        payload = {
            "referred_email": "luiza@gmail.com",
            "name": "Luiza",
            "document": "16221782031",
            "birth_date": "1998-10-10",
            "phone": "16675432678",
        }

        response = self.client.post(
            reverse("accept_referral"),
            data=json.dumps(payload),
            content_type="application/json",
        )

        decode_response = response.content.decode("utf-8")
        assert response.status_code == 400
        assert (
            "Esse email não foi indicado, verifique se você digitou corretamente"
            in decode_response
        )

    def test_accept_referral_already_have_been_accepted(self):
        Referral.objects.create(
            user=self.user, referred_email="luana@gmail.com", has_accepted=True
        )
        payload = {
            "referred_email": "luana@gmail.com",
            "name": "Luana",
            "document": "33552087010",
            "birth_date": "1998-10-10",
            "phone": "16875432678",
        }

        response = self.client.post(
            reverse("accept_referral"),
            data=json.dumps(payload),
            content_type="application/json",
        )

        decode_response = response.content.decode("utf-8")
        assert response.status_code == 400
        assert "Essa indicação já foi aceita ou não está mais ativa" in decode_response

    @freeze_time("2021-11-01")
    @patch("datetime.date.today", return_value=date(2022, 1, 1))
    def test_accept_referral_more_than_30_days(self, mock_today):
        Referral.objects.create(user=self.user, referred_email="luana@gmail.com")

        payload = {
            "referred_email": "luana@gmail.com",
            "name": "Luana",
            "document": "33552087010",
            "birth_date": "1998-10-10",
            "phone": "16875432678",
        }

        response = self.client.post(
            reverse("accept_referral"),
            data=json.dumps(payload),
            content_type="application/json",
        )

        decode_response = response.content.decode("utf-8")
        assert response.status_code == 400
        assert "Essa indicação já foi aceita ou não está mais ativa" in decode_response
