


# '''this is a custom command that can be called by using ./manage.py import_products
# the aim of this command is to import a json file in the database

import os
import json
from django.core.management import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from products.models import Product, Category, Image, Review, QuestionAnswer

AuthUserModel = get_user_model()

# join data and products with a function
def get_products_list():
    with open(os.path.join('data', 'products.json')) as products_file:
        products = json.load(products_file)
    return products


# define the custom command that parses and adds the
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--file', '-f', type=str)

    def handle(self, *args, **options):
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

        for product in products_list:
            # print (product["name"])
            # parsing through the json file to be able to make a class instance of product which is translated into a
            # the html view

            db_product = Product(
                name = product["name"],
                description = product["description"],
                size = product["size"],
                color = product["color"],
                price = product["price"],
                quantity = product ["quantity"],
            )
            print (db_product.name)
            db_product.save()

            # parse through the images using the dictionary key image, it's a class instance Image
            # save it in the data base
            for image in product["image"]:
                db_image = Image(
                image = image,
                    product = db_product
                    )
                # print (db_image.image)
            db_image.save()


# def create_superuser()