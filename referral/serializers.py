from rest_framework import serializers

from referral.models import Referral


class ReferralSerializer(serializers.ModelSerializer):
    created_date = serializers.ReadOnlyField()
    has_accepted = serializers.ReadOnlyField()

    class Meta:
        model = Referral
        fields = [
            "id",
            "user",
            "referred_email",
            "created_date",
            "has_accepted",
        ]  # noqa
