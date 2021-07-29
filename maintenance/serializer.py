from django.db import models
from rest_framework import serializers

from .models import Maintenance

class SerializerMaintenance(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'car_model', 'problem_description', 'technician',
'deliver_time')
        model = Maintenance