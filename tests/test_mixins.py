from unittest.mock import patch

import pytest
from buksu_framework.base import BaseService
from buksu_framework.mixins import (
    BaseMixin, ListMixin, CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, CRUDMixin
)


class TestService(BaseService, CRUDMixin):
    service = "test_service"
    global_params = {"global": "param"}


@pytest.fixture
def test_service():
    return TestService("test_realm", "test_token")


def test_base_mixin_init():
    service = TestService("test_realm", "test_token")
    assert service.service == "test_service"
    assert service.version == "v1"
    assert service.global_params == {"global": "param"}


def test_base_mixin_init_custom_version():
    service = TestService("test_realm", "test_token", version="v2")
    assert service.version == "v2"


@patch.object(BaseService, 'get')
def test_list_mixin(mock_get, test_service):
    test_service.list(params={"extra": "param"})
    mock_get.assert_called_once_with("", params={"global": "param", "extra": "param"})


@patch.object(BaseService, 'post')
def test_create_mixin(mock_post, test_service):
    test_service.create({"data": "value"}, params={"extra": "param"})
    mock_post.assert_called_once_with("", data={"data": "value"}, params={"global": "param", "extra": "param"})


@patch.object(BaseService, 'get')
def test_retrieve_mixin(mock_get, test_service):
    test_service.retrieve("123", params={"extra": "param"})
    mock_get.assert_called_once_with("123", params={"global": "param", "extra": "param"})


@patch.object(BaseService, 'put')
def test_update_mixin(mock_put, test_service):
    test_service.update("123", data={"data": "value"}, params={"extra": "param"})
    mock_put.assert_called_once_with("123", data={"data": "value"}, params={"global": "param", "extra": "param"})


@patch.object(BaseService, 'delete')
def test_delete_mixin(mock_delete, test_service):
    test_service.remove("123", params={"extra": "param"})
    mock_delete.assert_called_once_with("123", params={"global": "param", "extra": "param"})


def test_crud_mixin_inheritance():
    assert issubclass(CRUDMixin, BaseMixin)
    assert issubclass(CRUDMixin, ListMixin)
    assert issubclass(CRUDMixin, CreateMixin)
    assert issubclass(CRUDMixin, RetrieveMixin)
    assert issubclass(CRUDMixin, UpdateMixin)
    assert issubclass(CRUDMixin, DeleteMixin)


def test_crud_mixin_methods(test_service):
    methods = ['list', 'create', 'retrieve', 'update', 'remove']
    for method in methods:
        assert hasattr(test_service, method)
        assert callable(getattr(test_service, method))
