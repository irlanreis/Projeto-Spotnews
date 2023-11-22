from rest_framework import serializers
from news.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "role"]
