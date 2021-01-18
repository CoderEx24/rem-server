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

    return Response(f'Signup failed\n{form.errors}', status.HTTP_406_NOT_ACCEPTABLE)

