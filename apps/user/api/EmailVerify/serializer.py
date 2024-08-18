from rest_framework import serializers

from apps.user.models import User, VerifyEmail


class EmailVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyEmail
        fields = (
            "email",
            "code"
        )
