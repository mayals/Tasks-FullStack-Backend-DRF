"""
URL configuration for b_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path,include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from todoApp import views





# viewsets
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('tasks', views.TaskViewSet,basename="tasks")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    # admin path
    path('admin/', admin.site.urls),

    # api-auth path
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # ModelViewSet path
    path('api-viewset/', include(router.urls)),

]



    
   




