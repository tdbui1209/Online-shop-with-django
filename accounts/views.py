from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login as auth_login  # to avoid conflict with login function in views.py
from orders.models import Order, OrderItem


def login(request, user):
    return render(request, 'registration/login.html', {'user': user})

def signup(request):
    if request.method == 'GET':
        form = SignupForm()
        return render(request, 'registration/signup.html', {'form': form})
    elif request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('shop:product_list')
        else:
            return render(request, 'registration/signup.html', {'form': form})

def orders(request):
    orders = Order.objects.filter(user=request.user)
    orderitems = OrderItem.objects.filter(order__in=orders)
    orderitems_total_dict = {}  # to calculate total cost of each order
    for orderitem in orderitems:
        if orderitem.order.id in orderitems_total_dict:
            orderitems_total_dict[orderitem.order.id] += orderitem.get_cost()
        else:
            orderitems_total_dict[orderitem.order.id] = orderitem.get_cost()
    return render(request, 'accounts/orders.html', {'orders': orders, 'orderitems': orderitems, 'orderitems_total_dict': orderitems_total_dict})
