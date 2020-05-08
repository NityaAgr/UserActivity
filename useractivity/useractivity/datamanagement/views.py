from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseBadRequest
from django.http import JsonResponse
from django.core import serializers
import json

# Create your views here.
from . import models
from rest_framework import viewsets 
from rest_framework import permissions 
from datamanagement.serializers import UserSerializer , UserActivitySerializer

# ViewSet to display and fetch User details 

class UserViewSet (viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# ViewSet to display and fetch Activity period details 

class UserActivityViewSet (viewsets.ModelViewSet):
    queryset = models.UserActivity.objects.all()
    serializer_class = UserActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

# API View to GET and POST JSON data 
# Adds convenieve to test in POSTMAN

class UsersDetail(APIView):
    # POST method to retrieve user input data
    def post(self, request):
        # Fetch the JSON data jsondata
        jsondata = request.data
        users = request.data["members"]
       
        # To fetch values of respective key and save them in DB
        try:
            if jsondata["ok"] == True :
                for user in users :
                    person = models.User()
                    person.id = user["id"]
                    person.real_name = user["real_name"]
                    person.tz = user["tz"]
                    person.save()
                    for activity in user["activity_periods"]:
                        activityPeriod = models.UserActivity()
                        activityPeriod.start_time = activity["start_time"]
                        activityPeriod.end_time = activity["end_time"]
                        activityPeriod.user = person
                        # Insert the given values into the database.
                        activityPeriod.save()
                    return JsonResponse(jsondata, safe=False)
            else:
                return HttpResponseBadRequest("No JSON input present in right format")


        except Exception as e:
            return HttpResponseBadRequest(str(e))

    # GET method to display the posted data in JSON format
    def get(self, request):
        response = {}
        try:
            # To fetch data from save model data
            users = models.User.objects.all()
            users_activity = models.UserActivity.objects.all()
            
            print(users)
            userResponse = []
            for user in users :
                newUser = {}
                newUser["id"] = user.pk
                newUser["real_name"] = user.real_name
                newUser["tz"] = user.tz

                # In order to add user activity with respect to that specific user, it is filtered on the basis of user via FK in UserActivity DB
                activity = models.UserActivity.objects.filter(user=user)
                print(activity)
                activityArr = []
                for activity_period in users_activity:
                    newUserActivity = {}
                    newUserActivity["start_time"] = activity_period.start_time
                    newUserActivity["end_time"] = activity_period.end_time
                    activityArr.append(newUserActivity)
                newUser["activity_periods"] = activityArr
                userResponse.append(newUser)

            # To display the resultant output JSON data after looping through each key and fetching values
            response["ok"] = True
            response["members"] = userResponse

        except Exception as e:
            response["ok"] = False


            
        return JsonResponse(response, safe=False)
