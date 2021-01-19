from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, \
    permission_classes, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from .forms import *
from .models import *
from .serializers import *

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

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def api_get_incidents(req, maxsize=50):
    user_incidents = Incident.objects.filter(user=req.user)
    count = len(user_incidents)
    incidents = user_incidents[count - min(maxsize, count) : count]
    serializer = IncidentSerializer(incidents, many=True)
    return Response(serializer.data, status.HTTP_200_OK)

@api_view(['POST'])
@parser_classes([JSONParser])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def api_post_incident(req):
    serializer = IncidentSerializer(data=req.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(user=req.user)
    return Response(status=status.HTTP_202_ACCEPTED)
