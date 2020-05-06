from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseBadRequest

# Create your views here.
from . import models
from rest_framework import viewsets 
from rest_framework import permissions 
from datamanagement.serializers import UserSerializer , UserActivitySerializer

class UserViewSet (viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserActivityViewSet (viewsets.ModelViewSet):
    queryset = models.UserActivity.objects.all()
    serializer_class = UserActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

class Users(APIView):
    def post(self, request):
        response = {}

        users = request.data["members"]
        print(request.data["ok"])

       
        # try:
        for user in users :
            person = models.User()
            person.id = user["id"]
            person.real_name = user["real_name"]
            person.tz = user["tz"]
            person.save()
            for activity in user["activity_periods"]:
                activity_period = models.UserActivity()
                activity_period.start_time = activity["start_time"]
                activity_period.end_time = activity["end_time"]
                activity_period.user = person
                activity_period.save()


        
        # # except Exception as e :
        #     print(str(e))
        #     return HttpResponseBadRequest(str(e))
            
        return Response(response)

  