from django.core.management.base import BaseCommand
from shopapp.models import Customer, Product, Order


class Command(BaseCommand):
    help = "Delete data from DB tables"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Customer.objects.all().delete()
        Order.objects.all().delete()