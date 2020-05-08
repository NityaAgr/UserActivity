
from rest_framework import serializers

# importing model classes
from . import models

# Serializer call to fetch data from model and convert into Python datatype to render JSON

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class UserActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        user = UserSerializer(read_only=False)
        model = models.UserActivity
        fields = '__all__'

