from openpyxl import Workbook
from django.http import HttpResponse
from rest_framework import generics
from .serializers import RobotSerializer
from .models import Robot


class RobotCreateAPIView(generics.CreateAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


def generate_excel(request):
    wb = Workbook()

    robots_serials_data = dict()
    models = list()

    for robot in Robot.objects.all():
        if robot.model not in models:
            models.append(robot.model)

        if robot.serial in robots_serials_data:
            robots_serials_data[robot.serial] += 1
            continue
        robots_serials_data[robot.serial] = 1

    for model in models:
        ws = wb.create_sheet(f"{model}")
        ws.append(["Модель", "Версия", "Количество за неделю"])
        for robot_serial in robots_serials_data.keys():
            robot_serials_model = robot_serial.split("-")[0]
            robot_serials_version = robot_serial.split("-")[1]
            if model == robot_serials_model:
                ws.append(
                    [
                        robot_serials_model,
                        robot_serials_version,
                        robots_serials_data[robot_serial],
                    ]
                )

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="Report.xlsx"'

    wb.save(response)

    return response
