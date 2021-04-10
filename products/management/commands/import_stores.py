import os
import json
from django.core.management import BaseCommand, CommandError
from django.contrib.auth import get_user_model
# from products.models import Store

AuthUserModel = get_user_model()

def get_products_list():
    with open(os.path.join('data', 'products.json')) as products_file:
    products = json.load(products_file)
    return products

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--file','-f', type=str)

    def handle(self,*args, **options):
        file_path = options.get('file')

        if not_file_path:
            raise CommandError('File not provided!')

        if not file_path.endswith('.json'):
            raise CommandError('Import supports .json files only!')

        file_path = os.path.join('data', file_path)
        try:
            with open(file_path) as import_file:
                products = json.load(import_file)
        except FileNotFoundError as e:
            raise CommandError('File at %s was not found!' % file_path)

        product_list = get_products_list()


def create_superuser()