import pytest
from sole_market.models import Category

@pytest.fixture
def single_category(db):
    return Category.objects.create(name="example", slug="example")