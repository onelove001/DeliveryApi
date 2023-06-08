from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length = 30)
    email = serializers.EmailField(max_length = 50)
    phone = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length = 8, write_only=True    )

    class Meta:
        model = User
        fields = ["username", "email", "phone", "password"]


    def validate(self, attrs):
        username_exists = User.objects.filter(username = attrs["username"]).exists()
        email_exists = User.objects.filter(username = attrs["email"]).exists()
        phone_exists = User.objects.filter(username = attrs["phone"]).exists()
        
        if email_exists:
            raise serializers.ValidationError(detail="User with Email exists")

        if username_exists:
            raise serializers.ValidationError(detail="User with Username exists")

        if phone_exists:
            raise serializers.ValidationError(detail="User with Phone Number exists")

        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], email = validated_data["email"], phone = validated_data["phone"])
        user.set_password(validated_data["password"])
        user.save()
        return user