from email.mime import image
from pydoc import describe
import pytest
from sole_market.models import Category, Product

@pytest.fixture
def single_category(db):
    return Category.objects.create(name="example", slug="example")

@pytest.fixture
def single_product(db, single_category):
    return Product.objects.create(category=single_category, name="sample product", slug="sample-product", description=None, price=420.69, image=None)

