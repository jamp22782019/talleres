from rest_framework import viewsets
from .models import Ultrasonic
from .serializers import UltrasonicSerializer

class UltrasonicViewSet(viewsets.ModelViewSet):
    queryset = Ultrasonic.objects.all().order_by('-created')
    serializer_class = UltrasonicSerializer