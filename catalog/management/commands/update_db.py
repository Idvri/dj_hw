from django.core.management import BaseCommand
from django.db import connection
from catalog.models import Category, Product
import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Сбрасываю id в БД
        with connection.cursor() as cursor:
            cursor.execute("SELECT setval('catalog_category_id_seq', 1, false);"
                           "SELECT setval('catalog_product_id_seq', 1, false)")

        category_list = json.load(open('fixture_for_category.json', 'r', encoding='utf-8'))
        product_list = json.load(open('fixture_for_products.json', 'r', encoding='utf-8'))

        category_set = set()
        category_for_create = []
        products_for_create = []

        for category in category_list:
            category_set.add(category["fields"]["name"])

        for category in product_list:
            category_set.add(category["fields"]['category'])

        for category in category_set:
            category = {'name': category}
            category_for_create.append(Category(**category))

        Category.objects.bulk_create(category_for_create)

        for product in product_list:
            category = Category.objects.get(name=product['fields']['category'])
            product['fields']['category'] = category
            if product['fields']['preview'] is None:
                product['fields']['preview'] = 'placeholder.png'
                products_for_create.append(Product(**product['fields']))
            else:
                products_for_create.append(Product(**product['fields']))

        Product.objects.bulk_create(products_for_create)
