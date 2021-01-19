from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import *

@api_view(['POST'])
def api_signup(req):
    form = SignupForm(req.POST)
    if form.is_valid():
        form.save()
        return Response('Signup succeeded', status.HTTP_201_CREATED)

    return Response(f'Signup failed\n{form.error_messages}', status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['POST'])
def api_login(req):
    form = LoginForm(req, req.POST)
    if form.is_valid():
        return Response('Login succeeded', status.HTTP_202_ACCEPTED)
    return Response(f'Login failed {form.error_messages}', status.HTTP_406_NOT_ACCEPTABLE)

