from rest_framework import serializers
from .models import UserProfile
from .tasks import create_superadmin


class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=256)


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['email','name', 'password']

    def create(self, validate_data):
        instance = super(CreateUserSerializer, self).create(validate_data)
        create_superadmin.delay(str(instance.id))

        return instance