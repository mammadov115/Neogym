from rest_framework import serializers
from accounts.models import User
from rest_framework.validators import ValidationError


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=80)
    password = serializers.CharField(max_length=80, write_only = True)

    class Meta:
        model = User
        fields = "__all__"

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs["email"]).exists()

        if email_exists:
            raise ValidationError("Email has already been used")

        return super().validate(attrs)
    
