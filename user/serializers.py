from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    balance = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ["name", "document", "email", "birth_date", "phone", "balance"]
