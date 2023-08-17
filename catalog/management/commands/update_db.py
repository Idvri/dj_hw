import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_list = json.load(open('fixture_for_category.json', 'r'))
        product_list = json.load(open('fixture_for_products.json', 'r'))

        category_for_create = []
        products_for_create = []

        for category in category_list:
            category_for_create.append(Category(**category['fields']))

        for product in product_list:
            products_for_create.append(Product(**product['fields']))

        Category.objects.bulk_create(category_for_create)
        Product.objects.bulk_create(products_for_create)
