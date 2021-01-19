from rest_framework import serializers
from .models import *

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ['time', 'symptoms', 'diagnosis']

