import pytest

from sole_market.models import Category

"""
Tests written to check models.Category for CRUD operations
"""
# Create
@pytest.mark.db
def test_category_db_create(single_category):
    new_category = single_category
    assert new_category.id == Category.objects.all().first().id

# TODO: Read
# @pytest.mark.db
# def test_category_db_read(single_category):
#     # Category.objects.get(id=id)
#     pass

# TODO: Update
# @pytest.mark.db
# def test_category_db_update(single_category):
#     # Category.objects.filter(slug=slug)
#     pass

# TODO: Delete
# @pytest.mark.db
# def test_category_db_delete(single_category):
#     # Category.objects.get(id=id)
#     pass