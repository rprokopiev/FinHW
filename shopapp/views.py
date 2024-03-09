from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import logging
from .models import Customer, Product, Order
from .forms import AddProduct, EditProduct, ImageForm
from django.core.files.storage import FileSystemStorage


logger = logging.getLogger(__name__)


def index(request):
    logger.info('INDEX page raised')
    message = 'Welcome to ShopApp'
    return render(request, 'shopapp/index.html', context={'content': message})


def main(request):
    logger.info('MAIN page raised')
    message = 'Main Page of ShopApp'
    return render(request, 'shopapp/main.html', context={'content': message})


def about(request):
    logger.info('ABOUT page raised')
    message = 'About Page of ShopApp'
    return render(request, 'shopapp/main.html', context={'content': message})


def client_orders(request, phone):
    logger.info('client_order page')
    client = get_object_or_404(Customer, phone=phone)
    orders = Order.objects.filter(customer=client.pk).order_by('pk')
    context = {
        'customer': client,
        'orders': orders,
    }
    return render(request, 'shopapp/client_orders.html', context)


def client_products(request, phone):
    logger.info('client_products page')
    client = get_object_or_404(Customer, phone=phone)
    orders = Order.objects.filter(customer=client.pk).order_by('pk')
    products = [order.products.all() for order in orders]
    context = {
        'customer': client,
        'orders': orders,
        'products': products,
    }
    return render(request, 'shopapp/client_products.html', context)


def inventory(request):
    logger.info('inventory page')
    inventory = Product.objects.all().order_by('prod_name')
    return render(request, 'shopapp/inventory.html', context={'inventory': inventory})


def add_product(request):
    if request.method == 'POST':
        form = AddProduct(request.POST)
        if form.is_valid():
            prod_name = form.cleaned_data['prod_name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            new_product = Product(
                                prod_name=prod_name,
                                description=description,
                                price=price,
                                quantity=quantity,
                            )
            new_product.save()
            message = f'Product {new_product.prod_name} added'
    else:
        form = AddProduct()
        message = 'Fill the form'
    return render(request, 'shopapp/add_product.html', {'form': form, 'message': message})


def edit_product(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id) 
        # Product.objects.filter(id=product_id).first()
        form = EditProduct(request.POST)
        if form.is_valid():
            product.prod_name = form.cleaned_data['prod_name']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.quantity = form.cleaned_data['quantity']
            product.save()
            message = f'Product edited'
    else:
        form = EditProduct()
        message = 'Fill the form'
    return render(request, 'shopapp/edit_product.html', {'form': form, 'message': message})


def upload_image(request, product_id):
    product = get_object_or_404(Product, pk=product_id) 
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            product.image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(product.image.name, product.image)

    else:
        form = ImageForm()
    return render(request, 'shopapp/upload_image.html', {'form': form})