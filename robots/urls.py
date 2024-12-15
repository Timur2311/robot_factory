from django.urls import path
from .views import RobotCreateAPIView

urlpatterns = [
    path("", RobotCreateAPIView.as_view(), name="robot-create")
]
