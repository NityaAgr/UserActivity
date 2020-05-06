from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from . import models
from rest_framework import viewsets 
from rest_framework import permissions 
from datamanagement.serializers import UserSerializer, GroupSerializer, ActivitySerializer

class UserViewSet (viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer 
    permission_classes = [permissions.IsAuthenticated]

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = models.Activity.objects.all()
    serializer_class = ActivitySerializer 
    permission_classes = [permissions.IsAuthenticated]