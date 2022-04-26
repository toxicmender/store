import pytest
from rest_framework.test import APIClient

@pytest.fixture
def api_test_client():
    return APIClient()