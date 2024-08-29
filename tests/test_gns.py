from unittest.mock import patch

import pytest
from buksu_framework.services.gns import GlobalNotificationService


@pytest.fixture
def gns_service():
    return GlobalNotificationService("test_realm", "test_token")


@patch.object(GlobalNotificationService, 'get')
def test_list(mock_get, gns_service):
    gns_service.list(params={"page": 1})
    mock_get.assert_called_once_with("", params={"page": 1})


@patch.object(GlobalNotificationService, 'get')
def test_retrieve(mock_get, gns_service):
    gns_service.get("notification123")
    mock_get.assert_called_once_with("notification123")


@patch.object(GlobalNotificationService, 'post')
def test_read(mock_post, gns_service):
    gns_service.read("notification123")
    mock_post.assert_called_once_with("notification123/read")


@patch.object(GlobalNotificationService, 'post')
def test_unread(mock_post, gns_service):
    gns_service.unread("notification123")
    mock_post.assert_called_once_with("notification123/unread")


@patch.object(GlobalNotificationService, 'post')
def test_mark_all_as_read(mock_post, gns_service):
    gns_service.mark_all_as_read()
    mock_post.assert_called_once_with("mark-all-as-read")


@patch.object(GlobalNotificationService, 'post')
def test_mark_all_as_unread(mock_post, gns_service):
    gns_service.mark_all_as_unread()
    mock_post.assert_called_once_with("mark-all-as-unread")


@patch.object(GlobalNotificationService, 'post')
def test_notify(mock_post, gns_service):
    notification_data = {"message": "Test notification"}
    gns_service.notify("user123", notification_data)
    mock_post.assert_called_once_with("user123/notify", data=notification_data)


@patch.object(GlobalNotificationService, 'post')
def test_notify_group(mock_post, gns_service):
    notification_data = {"message": "Group notification"}
    gns_service.notify_group("group123", notification_data)
    mock_post.assert_called_once_with("group123/notify", data=notification_data)


@patch.object(GlobalNotificationService, 'post')
def test_notify_all(mock_post, gns_service):
    notification_data = {"message": "Global notification"}
    gns_service.notify_all(notification_data)
    mock_post.assert_called_once_with("notify-all", data=notification_data)


def test_service_name():
    assert GlobalNotificationService.service == "gns"


@patch.object(GlobalNotificationService, '__init__')
def test_inheritance(mock_init):
    mock_init.return_value = None
    service = GlobalNotificationService("test_realm", "test_token")
    assert isinstance(service, GlobalNotificationService)
    mock_init.assert_called_once_with("test_realm", "test_token")
