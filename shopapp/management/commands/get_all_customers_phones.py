from django.core.management.base import BaseCommand
from shopapp.models import Customer


class Command(BaseCommand):
    help = "Get all customers with phone numbers"

    def handle(self, *args, **options):
        customers = Customer.objects.all()
        for customer in customers:
            self.stdout.write(f'{customer.phone} - {customer}')
