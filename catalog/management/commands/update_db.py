from django.core.management import BaseCommand
from django.db import connection
from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Сбрасываю id в БД
        with connection.cursor() as cursor:
            cursor.execute("SELECT setval('catalog_category_id_seq', 1, false);"
                           "SELECT setval('catalog_product_id_seq', 1, false)")

        product_list = [
            {"name": "Orange",
             "overview": "",
             "preview": "orange.jpg",
             "category": "Fruits",
             "price": 25,
             "date_of_creation": "2023-08-17T13:47:17Z",
             "last_update": None},
            {"name": "Apple",
             "overview": "",
             "preview": "apple.jpg",
             "category": "Fruits",
             "price": 20,
             "date_of_creation": "2023-08-17T13:48:20Z",
             "last_update": None},
            {"name": "Banana",
             "overview": "",
             "preview": "banana.jpg",
             "category": "Fruits",
             "price": 10,
             "date_of_creation": "2023-08-17T13:48:43Z",
             "last_update": None},
            {"name": "IPhone 13",
             "overview": "",
             "preview": "iphone.jpg",
             "category": "Mobile",
             "price": 75000,
             "date_of_creation": "2023-08-17T13:49:10Z",
             "last_update": None}
        ]

        category_set = set()
        category_for_create = []
        products_for_create = []

        for category in product_list:
            category_set.add(category['category'])

        for category in category_set:
            category = {'name': category}
            category_for_create.append(Category(**category))

        Category.objects.bulk_create(category_for_create)

        for product in product_list:
            category = Category.objects.get(name=product['category'])
            product['category'] = category
            products_for_create.append(Product(**product))

        Product.objects.bulk_create(products_for_create)
