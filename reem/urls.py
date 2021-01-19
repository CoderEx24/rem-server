from django.urls import path, include
from .views import *

app_name = 'reem'
urlpatterns = [
    path('signup/', api_signup, name='signup'),
    path('login/', api_login, name='login'),
    path('incident/get/<int:maxsize>/', api_get_incidents, name='get_incidents'),
]
