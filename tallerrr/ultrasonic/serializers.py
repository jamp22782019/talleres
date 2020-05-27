from rest_framework import serializers
from .models import Ultrasonic

class UltrasonicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ultrasonic
        fields = ('id', 'type', 'value')