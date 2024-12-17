# home/views.py
from django.shortcuts import render, redirect

def home(request):
    user_type = None
    if request.method == 'POST':
        user_type = request.POST.get('user_type')  # Get the selected user type
        if user_type == 'programmer':
            return redirect('programmer')  # Redirect to the programmer page
        elif user_type == 'director':
            return redirect('director')  # Redirect to the director page
        elif user_type == 'customer':
            return redirect('customer')  # Redirect to the customer page
    
    return render(request, 'home/home.html', {'user_type': user_type})


# Views for each user type
def programmer(request):
    return render(request, 'home/programmer.html')

def director(request):
    return render(request, 'home/director.html')

def customer(request):
    return render(request, 'home/customer.html')
