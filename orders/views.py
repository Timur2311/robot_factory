from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Order
from customers.models import Customer
from robots.models import Robot
from .forms import OrderForm


def order_view(request):
    message = ""
    order_accepted = False
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            robot_model = form.cleaned_data['robot_model']
            robot_version = form.cleaned_data['robot_version']
            email = form.cleaned_data['email']

            
            message = "Такого робота нет, но как только он будет доступен , мы вам сообщим."
            order_accepted = False
            robots = Robot.objects.filter(model=robot_model, version=robot_version)
            if robots.exists():
                message = "Ваш заказ получен"
                order_accepted = True

            order = Order(customer=Customer.objects.create(email=email),
                          robot_serial=f"{robot_model}-{robot_version}")
            order.save()
            form = OrderForm()
            
    else:
        form = OrderForm()

    return render(request, 'home/customer.html', {'form': form, 'message': message, 'order_accepted': order_accepted})
