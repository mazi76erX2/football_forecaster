from typing import Dict, Union, Tuple

from rest_framework.fields import EmailField, CharField
from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email: EmailField = serializers.EmailField(
        required=True
    )
    username: CharField = serializers.CharField()
    password: CharField = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model: User = User
        fields: Tuple[str]  = ('email', 'username', 'password')
        extra_kwargs: Dict[str, Dict[str, bool]] = {'password': {'write_only': True}}

        """[summary]
        """    def create(self, validated_data: Dict[str, str]):
        password: str or None = validated_data.pop('password', None)
        instance: Union[User, User] = self.Meta.model(**validated_data)  #  as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserRegisterSerializer(serializers.ModelSerializer):
    email: EmailField = serializers.EmailField(
        required=True
    )
    phone_number: CharField = serializers.CharField()
    username: CharField = serializers.CharField()
    password: CharField = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User = User
        fields: Tuple[str] = ('email', 'username', 'password')
        extra_kwargs: Dict[str, Dict[str, bool]] = {'password': {'write_only': True}}

    def create(self, validated_data: Dict[str, str]):
        password: str or None = validated_data.pop('password', None)
        instance: Union[User, User] = self.Meta.model(**validated_data)  #  as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
            userprofile, created = UserProfile.objects.get_or_create(user=instance)
            userprofile.phone_number = validated_data['phone_number']
            userprofile.save()
        instance.save()
        return instance