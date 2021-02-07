from django.db import models

class Incident(models.Model):
    time = models.DateTimeField(auto_now=True, editable=False)
    symptoms = models.CharField(max_length=41)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=100, null=True)

