from email.mime import image
from pydoc import describe
import pytest
from sole_market.models import Category, Product


@pytest.fixture
def single_category(db):
    return Category.objects.create(name="example", slug="example")


@pytest.fixture
def populate_category(db, category_factory, num=3):
    # return Category.objects.create(name="example", slug="example")
    records = category_factory.create_batch(num)
    print(records)
    return records


# https://docs.pytest.org/en/stable/deprecations.html#calling-fixtures-directly
@pytest.fixture
def single_product(db, single_category):
    return Product.objects.create(
        category=single_category,
        name="sample product",
        slug="sample-product",
        description=None,
        price=420.69,
        image=None,
    )


@pytest.fixture
def populate_product(db, product_factory, category_factory, num=3):
    records = product_factory.create_batch(size=num)
    return records
