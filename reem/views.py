from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .forms import *

@api_view(['POST'])
def api_signup(req):
    form = SignupForm(req.POST)
    if form.is_valid():
        new_user = form.save()
        new_token, _ = Token.objects.get_or_create(user=new_user)
        return Response(f'Token {new_token}', status.HTTP_201_CREATED)

    return Response(f'{form.error_messages}', status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['POST'])
def api_login(req):
    form = LoginForm(req, req.POST)
    if form.is_valid():
        logged_user = form.get_user()
        new_token, _ = Token.objects.get_or_create(user=logged_user)
        return Response(f'Token {new_token}', status.HTTP_202_ACCEPTED)
    return Response(f'{form.error_messages}', status.HTTP_406_NOT_ACCEPTABLE)

