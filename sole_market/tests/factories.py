import factory
from pytest_factoryboy import register
from faker import Faker
from random import randrange

from sole_market.models import Category, Product

fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = fake.lexify(text="cat name ?????")
    slug = fake.lexify(text="cat-slug-?????".lower())


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    category = factory.SubFactory(CategoryFactory, slug=factory.SelfAttribute('..slug'))
    name = fake.lexify(text="prod name ?????")
    slug = fake.lexify(text="prod-slug-?????".lower())
    description = fake.text()
    price = randrange(50, 9999999) + (0.11 * randrange(0, 9))
    date_added = "2022-04-25T07:00:00.000000+05:30"


register(CategoryFactory)
register(ProductFactory)
