from django.urls import path, include
from .views import *

app_name = 'reem'
urlpatterns = [
    path('signup/', api_signup, name='signup'),
]
