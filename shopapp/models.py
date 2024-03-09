from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12, unique=True)
    address = models.CharField(max_length=120)
    reg_date = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=True)

    def __str__(self):
        return f'Customer Name: {self.name}, email: {self.email}'
    

class Product(models.Model):
    prod_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()
    add_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/', blank=True)

    def __str__(self):
        return f'Product Name: {self.prod_name}, price: {self.price}, quantity left: {self.quantity}'


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'Order date: {self.order_date}, Amount: {self.amount}, Customer: {self.customer}'
    
    def total_amount(self):
        self.amount = sum(product.price for product in self.products.all())
        self.save()