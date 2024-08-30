from unittest.mock import patch

import pytest

from buksu_framework.base import BaseService
from buksu_framework.mixins import CRUDMixin
from buksu_framework.services.ums import UserMediaService


@pytest.fixture
def ums_service():
    return UserMediaService("test_realm", "test_token")


@patch.object(UserMediaService, 'get')
def test_list(mock_get, ums_service):
    ums_service.list(params={"page": 1})
    mock_get.assert_called_once_with("", params={"storage": "local", "page": 1})


@patch.object(UserMediaService, 'get')
def test_retrieve(mock_get, ums_service):
    ums_service.get("media123", params={"storage": "local"})
    mock_get.assert_called_once_with("media123", params={"storage": "local"})


@patch.object(UserMediaService, 'post')
def test_create(mock_post, ums_service):
    media_data = {"file_name": "test.jpg", "file_type": "image/jpeg"}
    ums_service.create(media_data)
    mock_post.assert_called_once_with("", data=media_data, params={"storage": "local"})


@patch.object(UserMediaService, 'put')
def test_update(mock_put, ums_service):
    media_data = {"file_name": "updated.jpg"}
    ums_service.update("media123", data=media_data)
    mock_put.assert_called_once_with("media123", data=media_data, params={"storage": "local"})


@patch.object(UserMediaService, 'delete')
def test_delete(mock_delete, ums_service):
    ums_service.delete("media123", params={"storage": "local"})
    mock_delete.assert_called_once_with("media123", params={"storage": "local"})


def test_service_name():
    assert UserMediaService.service == "ums"


def test_global_params():
    assert UserMediaService.global_params == {"storage": "local"}


@patch.object(UserMediaService, '__init__')
def test_inheritance(mock_init):
    mock_init.return_value = None
    service = UserMediaService("test_realm", "test_token")
    assert isinstance(service, UserMediaService)
    mock_init.assert_called_once_with("test_realm", "test_token")


def test_crud_mixin_inheritance():
    assert issubclass(UserMediaService, BaseService)
    assert issubclass(UserMediaService, CRUDMixin)
