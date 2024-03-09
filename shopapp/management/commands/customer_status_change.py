from django.core.management.base import BaseCommand
from shopapp.models import Customer


class Command(BaseCommand):
    help = "Mark customer as inactive or active per phone number"

    def add_arguments(self, parser):
        parser.add_argument('phone', type=str, help='Phone Number')

    def handle(self, *args, **kwargs):
        phone = kwargs.get('phone')
        customer = Customer.objects.filter(phone=phone).first()
        if customer.isactive == True:
            customer.isactive = False
            customer.save()
            self.stdout.write(f'{customer.name} with {customer.phone} has been inactived')
        else:
            customer.isactive = True
            customer.save()
            self.stdout.write(f'{customer.name} with {customer.phone} is active again now')