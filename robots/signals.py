from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Robot
from orders.models import Order
from .tasks import send_message_to_customer

def generate_serial(model, version):
    return f"{model}-{version}"


@receiver(pre_save, sender=Robot)
def pre_save_robot(sender, instance, **kwargs):
    robot_model = instance.model
    robot_version = instance.version
    serial = generate_serial(robot_model, robot_version)
    instance.serial = serial
    
    is_robot_exists = Robot.objects.filter(serial=serial).exists()

    if (
        order := Order.objects.filter(robot_serial=serial)
        .select_related("customer")
        .first()
    ):
        if not is_robot_exists:
            send_message_to_customer.delay(robot_model, robot_version, order.customer.email)


  