from rest_framework import generics
from .serializers import RobotSerializer
from .models import Robot


class RobotCreateAPIView(generics.CreateAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
