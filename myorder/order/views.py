from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from .models import Order
# Create your views here.
def index(request):
    return render(request, 'order/index.html')

def add_order(request):
    if request.method == 'GET':
        return render(request,'order/order_form.html')
    else :
        order_text = request.POST['order_text']
        price = request.POST['price']
        address = request.POST['address']

        Order.objects.create(
            order_text = order_text,
            price = price,
            address = address
        )
        return HttpResponseRedirect('/order/')

def order_list(request):
    order_list = Order.objects.all()
    return render(request, 'order/order_list.html',{'order_list':order_list})

def delete(request, id):
    Order.objects.get(id = id).delete()
    return HttpResponseRedirect('/order/order_list/')

def update(request,id):
    order = Order.objects.get(id = id)
    
    if request.method == 'GET': 
        return render(request, 'order/update_form.html', {'order':order})
    else:
        order.order_text = request.POST['order_text']
        order.price = request.POST['price']
        order.address = request.POST['address']
        order.save()
        return HttpResponseRedirect('/order/order_list/')

def search(request):
    get_text = request.GET['order_text']
    select = request.GET['option']

    order_list = []
    if select == 'full':
        order_list = Order.objects.filter(order_text = get_text)
    elif select == 'part':
        order_list = Order.objects.filter(order_text__contains = get_text)
    elif select == 'front':
        order_list = Order.objects.filter(order_text__startswith = get_text)

    print('aa')

    return render(request, 'order/order_list.html', {'order_list':order_list})
        
def show(request, id):
    order = Order.objects.get(id = id)
    context = {
        'order': order,
        'text_list' : order.order_text.split(',')
    }
    
    return render(request, 'order/order_show.html', context)

