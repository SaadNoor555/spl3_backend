from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', signin, name='signin'),
]

