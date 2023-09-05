from django.shortcuts import render,redirect,get_object_or_404
from menu.models import Dish 
from .forms import DishForm,OrderForm
from .models import Order, OrderItem

# Create your views here.
def dish_list(request):
    dishes=Dish.objects.all()
    return render(request,"list_dishes.html",{'dishes':dishes})



def add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish_list')  # Redirect to the dish list page
    else:
        form = DishForm()
    return render(request, 'add_dish.html', {'form': form})



def delete_dish(request, dish_id):
    dish = get_object_or_404(Dish, dish_id=dish_id)
    if request.method == 'POST':
        dish.delete()
        return redirect('dish_list')  # Redirect to the dish list page
    return render(request, 'delete_dish.html', {'dish': dish})


def update_dish(request, dish_id):
    dish = get_object_or_404(Dish, dish_id=dish_id)
    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('dish_list')  # Redirect to the dish list page
    else:
        form = DishForm(instance=dish)
    return render(request, 'update_dish.html', {'form': form, 'dish': dish})




def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('order_detail', order_id=order.order_id)
    else:
        form = OrderForm()
    return render(request, 'place_order.html', {'form': form})



def order_detail(request, order_id):
    order = Order.objects.get(pk=order_id)
    total_price = sum(order_item.dish.price * order_item.quantity for order_item in order.orderitem_set.all())
    if request.method == 'POST':
        new_status = request.POST.get('status')
        order.status = new_status
        order.save()

    context = {'order': order,'total_price':total_price}
    return render(request, 'order_details.html', context)






def order_list(request):
    orders = Order.objects.all()

    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        new_status = request.POST.get('status')
        
        try:
            order = Order.objects.get(pk=order_id)
            order.status = new_status
            order.save()
        except Order.DoesNotExist:
            print(f"Order with ID {order_id} does not exist.")

    context = {'orders': orders}
    return render(request, 'order_list.html', context)



def update_order_status(request, order_id):
    if request.method == 'POST':
        new_status = request.POST.get('status')
        try:
            order = Order.objects.get(pk=order_id)
            order.status = new_status
            order.save()
        except Order.DoesNotExist:
            pass  # Handle error if needed
    return redirect('order_list')  # Redirect back to order list page

def delete_order(request, order_id):
    if request.method == 'POST':
        try:
            order = Order.objects.get(pk=order_id)
            order.delete()
        except Order.DoesNotExist:
            pass  # Handle error if needed
    return redirect('order_list')  # Redirect back to order list page



    



