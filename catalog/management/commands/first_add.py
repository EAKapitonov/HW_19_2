from django.core.management import BaseCommand
from django.db import DEFAULT_DB_ALIAS

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        category_list = [
            {'category_name': 'Фрукты', 'translator': 'Категория фрукты'},
            {'category_name': 'Овощи', 'translator': 'Категория овощи'},
            {'category_name': 'Молочная продукция', 'translator': 'Категория молочная продукция'},
            {'category_name': 'Мясная продукция', 'translator': 'Категория мясная продукция'},
        ]
        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))
        Category.objects.bulk_create(category_for_create)



