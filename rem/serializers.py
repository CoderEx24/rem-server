from rest_framework import serializers
from .models import *

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ['symptoms']
        read_only_fields = ['time', 'diagnosis']

