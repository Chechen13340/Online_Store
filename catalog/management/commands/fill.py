from django.core.management import BaseCommand

from catalog.models import Product, Category
from pathlib import Path


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_list = [
            {'name': 'Вакуумное оборудование',
             'describe': 'Категория, которая содержит продукты относящиеся к вакуумной технике'},
            {'name': 'Аналитическое оборудование',
             'describe': 'Оборудование для диагностики плазмы'},
            {'name': 'Регуляторы расхода газа',
             'describe': 'Оборудование для газораспределительных систем. Для точной подачи необходимого расхода газа'}
        ]
        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)

        products_list = [
            {'name': 'Турбомолекулярный насос',
             'describe': 'Высоковакуумный насос сухой откачки. Химически стойкий.', 'preview': '',
             'category': 'Вакуумное оборудование', 'cost': 759000},
            {'name': 'Зонд Ленгмюра',
             'describe': 'Устройство для диагностики плазмы.', 'preview': '',
             'category': 'Аналитическое оборудование', 'cost': 978000
             },
            {'name': 'Насос Рутса',
             'describe': 'Насос для предварительной сухой откачки. Предельное давление 0.5 Па.', 'preview': '',
             'category': 'Вакуумное оборудование', 'cost': 250000
             },
            {'name': 'Osean Optics HR 4000',
             'describe': 'Оптический эмиссионный спектрометр. Диапазон длин волн 180 - 1200 нм.', 'preview': '',
             'category': 'Аналитическое оборудование', 'cost': 678000
             },
            {'name': 'РРГ-12',
             'describe': 'Регулятор расхода газа. Элточприбор. Максимальнйы расход 9 л/ч по Азоту.', 'preview': '',
             'category': 'Регуляторы расхода газа', 'cost': 60000
             },
            {'name': 'Horriba',
             'describe': 'Регулятор расхода газа в химически стойком исполнении. Время отклика 10 мс. Расход газа по азоту 9 л/ч.',
             'preview': '', 'category': 'Регуляторы расхода газа', 'cost': 200000
             }

        ]

        product_for_create = []
        for product_item in products_list:
            product_for_create.append(Product(**product_item))

        Product.objects.bulk_create(product_for_create)
