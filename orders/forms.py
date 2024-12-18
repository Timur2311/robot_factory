from django import forms

class OrderForm(forms.Form):
    robot_model = forms.CharField(max_length=2, required=True, label="Robot Model")
    robot_version = forms.CharField(max_length=2, required=True, label="Robot Version")
    email = forms.EmailField(required=True, label="Your Email")
