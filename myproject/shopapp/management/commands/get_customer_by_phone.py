from django.core.management.base import BaseCommand, CommandParser
from shopapp.models import Customer


class Command(BaseCommand):
    help = "Get customer by phone number"

    def add_arguments(self, parser):
        parser.add_argument('phone', type=str, help='Phone Number')

    def handle(self, *args, **kwargs):
        phone = kwargs['phone']
        customer = Customer.objects.filter(phone=phone).first()
        self.stdout.write(f'{customer}')