from unittest.mock import patch

import pytest
from buksu_framework.services.uas import UserAuthService


@pytest.fixture
def uas_service():
    return UserAuthService("test_realm", "test_token")


@patch.object(UserAuthService, 'post')
def test_register(mock_post, uas_service):
    uas_service.register("test@example.com", "password", {"name": "Test User"})
    mock_post.assert_called_once_with("register",
                                      data={"email": "test@example.com", "password": "password", "name": "Test User"})


@patch.object(UserAuthService, 'post')
def test_login(mock_post, uas_service):
    uas_service.login("test@example.com", "password")
    mock_post.assert_called_once_with("login", data={"email": "test@example.com", "password": "password"})


@patch.object(UserAuthService, 'post')
def test_logout(mock_post, uas_service):
    uas_service.logout("test_token")
    mock_post.assert_called_once_with("logout", data={"token": "test_token"})


@patch.object(UserAuthService, 'post')
def test_verify_otp(mock_post, uas_service):
    uas_service.verify_otp("test@example.com", "123456")
    mock_post.assert_called_once_with("verify-otp", data={"email": "test@example.com", "otp": "123456"})


@patch.object(UserAuthService, 'post')
def test_verify_email(mock_post, uas_service):
    uas_service.verify_email("test@example.com", "verification_token")
    mock_post.assert_called_once_with("verify-email", data={"email": "test@example.com", "token": "verification_token"})


@patch.object(UserAuthService, 'post')
def test_social_register(mock_post, uas_service):
    uas_service.social_register("google", "social_token")
    mock_post.assert_called_once_with("social-register", data={"provider": "google", "token": "social_token"})


@patch.object(UserAuthService, 'post')
def test_social_login(mock_post, uas_service):
    uas_service.social_login("facebook", "social_token")
    mock_post.assert_called_once_with("social-login", data={"provider": "facebook", "token": "social_token"})


@patch.object(UserAuthService, 'post')
def test_forgot_password(mock_post, uas_service):
    uas_service.forgot_password("test@example.com")
    mock_post.assert_called_once_with("forgot-password", data={"email": "test@example.com"})


@patch.object(UserAuthService, 'post')
def test_reset_password(mock_post, uas_service):
    uas_service.reset_password("test@example.com", "new_password", "reset_token")
    mock_post.assert_called_once_with("reset-password", data={"email": "test@example.com", "password": "new_password",
                                                              "token": "reset_token"})


@patch.object(UserAuthService, 'post')
def test_change_password(mock_post, uas_service):
    uas_service.change_password("test@example.com", "old_password", "new_password")
    mock_post.assert_called_once_with("change-password", data={"email": "test@example.com", "password": "old_password",
                                                               "new_password": "new_password"})


@patch.object(UserAuthService, 'post')
def test_refresh_token(mock_post, uas_service):
    uas_service.refresh_token("old_token")
    mock_post.assert_called_once_with("refresh-token", data={"token": "old_token"})


@patch.object(UserAuthService, 'post')
def test_get_access_token(mock_post, uas_service):
    uas_service.get_access_token("refresh_token")
    mock_post.assert_called_once_with("access-token", data={"token": "refresh_token"})


def test_service_name():
    assert UserAuthService.service_name == "uas"


@patch.object(UserAuthService, '__init__')
def test_inheritance(mock_init):
    mock_init.return_value = None
    service = UserAuthService("test_realm", "test_token")
    assert isinstance(service, UserAuthService)
    mock_init.assert_called_once_with("test_realm", "test_token")
