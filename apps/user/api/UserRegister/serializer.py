from rest_framework import serializers

from apps.user.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=16, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=16, write_only=True)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
            "password2"
        )
    

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.pop("password2")

        if password != password2:
            raise serializers.ValidationError({"error": "Passwords are not the same!"})
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

