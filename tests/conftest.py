import pytest
from rest_framework.test import APIClient

pytest_plugins = 'test.factories'


@pytest.fixture()
def client() -> APIClient:
    return APIClient()


@pytest.fixture()
def auth_client(client, user):
    client.force_login(user)
    return client
