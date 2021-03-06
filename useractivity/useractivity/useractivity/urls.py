"""useractivity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Import dependencies.

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# Import views.py from DataManagement app

from datamanagement import views

router = routers.DefaultRouter()

# Route to the User and UserActivity ViewSet

router.register(r'user', views.UserViewSet)
router.register(r'useractivity', views.UserActivityViewSet)

# 'viewall/' path added to fetch API results

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('viewall/', views.UsersDetail.as_view()),
]
