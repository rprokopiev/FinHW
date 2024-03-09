from django.core.management.base import BaseCommand
from shopapp.models import Customer, Product, Order
from random import randint, choice


class Command(BaseCommand):
    help = """Generates given amount of Products, Cutomers and random (1-5) amount of Orders for each customer"""
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        # generate Products
        for i in range(count):
            product = Product(
                prod_name = f'Prod<-{i}->Name>',
                description = f'Prod<-{i}->Description>',
                price = randint(1, 100),
                quantity = randint(50, 100),
            )
            product.save()
        inventory = Product.objects.all()

        # generate Cusomers
        for i in range(count):
            customer = Customer(
                name = f'Cust<-{i}->Name>',
                email = f'Cust<-{i}->@mail.ru>',
                phone = f'{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}Cust{i}',
                address = f'Cust<-{i}->Address>',
            )
            customer.save()

            # generate Orders for the Customer
            for _ in range(randint(1, 5)):
                order = Order(
                    customer = customer,
                    amount = 0,
                )
                order.save()
                for _ in range(randint(1, 10)):
                    order.products.add(choice(inventory))
                order.total_amount()
                
