'''this is a custom command that can be calleed by using ./manage.py import_products
the aim of this command is to import a json file in the database'''

import os
import json
from django.core.management import BaseCommand, CommandError
from django.contrib.auth import get_user_model

AuthUserModel = get_user_model()


def get_products_list():
    with open(os.path.join('data', 'products.json')) as products_file:
        products = json.load(products_file)
        return products

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('pe=str)

    def handle(self,*args, **options):
        file_path = options.get('file')

        if not file_path:
            raise CommandError('File not provided!')

        if not file_path.endswith('.json'):
            raise CommandError('Import supports .json files only!')
        # if the file you try to import is not json this error is raised use ./manage.py import_products -f abc to test

        file_path = os.path.join('data', file_path)
        try:
            with open(file_path) as import_file:
                products = json.load(import_file)
        except FileNotFoundError as e:
            raise CommandError('File at %s was not found!' % file_path)

products_list = get_products_list()

print("products_list", products_list)


# def create_superuser()