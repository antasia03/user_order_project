from rest_framework import serializers
from .models import CustomUser, Order


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email', 'age']

    def validate_email(self, value):
        user = self.instance
        if user and user.email == value:
            return value

        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                'The user with this email already exists.'
            )
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user


class OrderSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'title', 'description', 'user']


class OrderCreationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        required=True
    )

    class Meta:
        model = Order
        fields = ['id', 'title', 'description', 'user']
