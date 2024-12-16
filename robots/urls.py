from django.urls import path
from .views import RobotCreateAPIView, generate_excel

urlpatterns = [
    path("", RobotCreateAPIView.as_view(), name="robot-create"),
    path("get-report/", generate_excel, name="generate_excel"),
]
