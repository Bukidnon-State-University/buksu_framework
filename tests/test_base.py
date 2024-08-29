from unittest.mock import patch

import pytest

from buksu_framework.api_client import StandardAPIClient
from buksu_framework.base import BaseService
from buksu_framework.mixins import BaseMixin


class TestService(BaseService):
    service = "test_service"
    version = "v1"


@pytest.fixture
def base_service():
    return TestService("test_realm", "test_token")


def test_base_service_inheritance():
    assert issubclass(BaseService, StandardAPIClient)
    assert issubclass(BaseService, BaseMixin)


def test_base_service_init(base_service):
    assert base_service.realm == "test_realm"
    assert base_service.access_token == "test_token"
    assert base_service.service == "test_service"
    assert base_service.version == "v1"


def test_base_service_init_custom_version():
    custom_service = TestService("test_realm", "test_token", version="v2")
    assert custom_service.version == "v2"


@patch.object(StandardAPIClient, '__init__')
def test_base_service_super_init(mock_init):
    TestService("test_realm", "test_token")
    mock_init.assert_called_once_with("test_realm", "test_token", "test_service", version="v1")


@patch.object(StandardAPIClient, '__init__')
def test_base_service_super_init_custom_version(mock_init):
    TestService("test_realm", "test_token", version="v2")
    mock_init.assert_called_once_with("test_realm", "test_token", "test_service", version="v2")


def test_base_service_inherits_standard_api_client_methods(base_service):
    methods = ['get', 'post', 'put', 'delete']
    for method in methods:
        assert hasattr(base_service, method)
        assert callable(getattr(base_service, method))
