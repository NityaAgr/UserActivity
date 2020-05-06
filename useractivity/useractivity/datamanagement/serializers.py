
from rest_framework import serializers
from . import models
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'



class UserActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.UserActivity
        fields = '__all__'