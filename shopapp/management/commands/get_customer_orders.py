from django.core.management.base import BaseCommand
from shopapp.models import Customer, Order


class Command(BaseCommand):
    help = "Get orders by customer phone number"

    def add_arguments(self, parser):
        parser.add_argument('phone', type=str, help='Phone Number')

    def handle(self, *args, **kwargs):
        phone = kwargs.get('phone')
        customer = Customer.objects.filter(phone=phone).first()
        if customer is not None:
            orders = Order.objects.filter(customer=customer)
            for order in orders: 
                self.stdout.write(f'{order}')
                for product in order.products.all():
                    self.stdout.write(f'{product}')
        else:
            self.stdout.write(f'{customer}')