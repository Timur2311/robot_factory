from rest_framework import serializers
from .models import Robot
from rest_framework.exceptions import ValidationError


class RobotSerializer(serializers.ModelSerializer):
    serial = serializers.CharField(read_only=True)

    class Meta:
        model = Robot
        fields = ("serial", "model", "version", "created")

    def validate(self, attrs):
        model = attrs.get("model")
        version = attrs.get("version")
        created = attrs.get("created")

        if Robot.objects.filter(model=model, version=version, created=created).exists():
            raise ValidationError(
                {"non_field_errors": ["Combination of fields must be unique."]}
            )

        return attrs
