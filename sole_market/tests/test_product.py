import pytest

from sole_market.models import Product

"""
Tests written to check models.Product for CRUD operations
"""
# Create
@pytest.mark.db
def test_product_db_create(single_product):
    new_product = single_product
    assert new_product.id == Product.objects.all().first().id


# TODO: Read
# @pytest.mark.db
# def test_product_db_read(single_product):
#     # Product.objects.get(id=id)
#     pass

# TODO: Update
# @pytest.mark.db
# def test_product_db_update(single_product):
#     # Product.objects.filter(slug=slug)
#     pass

# TODO: Delete
# @pytest.mark.db
# def test_product_db_delete(single_product):
#     # Product.objects.get(id=id)
#     pass
