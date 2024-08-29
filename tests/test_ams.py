from unittest.mock import patch

import pytest

from buksu_framework.services.ams import AccountManagementService


@pytest.fixture
def ams_service():
    return AccountManagementService("test_realm", "test_token")


@patch.object(AccountManagementService, 'post')
def test_register_user(mock_post, ams_service):
    user_data = {"username": "testuser", "email": "test@example.com"}
    ams_service.register_user(user_data)
    mock_post.assert_called_once_with("register", data=user_data)


@patch.object(AccountManagementService, 'get')
def test_profile(mock_get, ams_service):
    ams_service.profile("user123")
    mock_get.assert_called_once_with("user123/profile")


@patch.object(AccountManagementService, 'put')
def test_update_profile(mock_put, ams_service):
    profile_data = {"name": "Test User", "bio": "Test bio"}
    ams_service.update_profile("user123", profile_data)
    mock_put.assert_called_once_with("user123/profile", data=profile_data)


@patch.object(AccountManagementService, 'get')
def test_get_user_by_email(mock_get, ams_service):
    ams_service.get_user_by_email("test@example.com")
    mock_get.assert_called_once_with("user-by-email/test@example.com")


@patch.object(AccountManagementService, 'put')
def test_change_password(mock_put, ams_service):
    password_data = {"old_password": "old", "new_password": "new"}
    ams_service.change_password("user123", password_data)
    mock_put.assert_called_once_with("user123/change-password", data=password_data)


@patch.object(AccountManagementService, 'get')
def test_get_social_accounts(mock_get, ams_service):
    ams_service.get_social_accounts("user123")
    mock_get.assert_called_once_with("user123/social-accounts")


@patch.object(AccountManagementService, 'post')
def test_add_social_account(mock_post, ams_service):
    social_data = {"provider": "google", "token": "abc123"}
    ams_service.add_social_account("user123", social_data)
    mock_post.assert_called_once_with("user123/social-accounts", data=social_data)


@patch.object(AccountManagementService, 'delete')
def test_remove_social_account(mock_delete, ams_service):
    ams_service.remove_social_account("user123", "google")
    mock_delete.assert_called_once_with("user123/social-accounts/google")


@patch.object(AccountManagementService, 'post')
def test_verify_otp(mock_post, ams_service):
    ams_service.verify_otp("user123", "123456")
    mock_post.assert_called_once_with("user123/verify-otp", data={"otp": "123456"})


@patch.object(AccountManagementService, 'post')
def test_setup_otp(mock_post, ams_service):
    ams_service.setup_otp("user123")
    mock_post.assert_called_once_with("user123/setup-otp")


@patch.object(AccountManagementService, 'delete')
def test_remove_otp(mock_delete, ams_service):
    ams_service.remove_otp("user123")
    mock_delete.assert_called_once_with("user123/otp")


@patch.object(AccountManagementService, 'put')
def test_activate_user(mock_put, ams_service):
    ams_service.activate_user("user123")
    mock_put.assert_called_once_with("user123/activate")


@patch.object(AccountManagementService, 'put')
def test_deactivate_user(mock_put, ams_service):
    ams_service.deactivate_user("user123")
    mock_put.assert_called_once_with("user123/deactivate")


@patch.object(AccountManagementService, 'delete')
def test_delete_account(mock_delete, ams_service):
    ams_service.delete_account("user123")
    mock_delete.assert_called_once_with("user123")


@patch.object(AccountManagementService, 'get')
def test_get_roles(mock_get, ams_service):
    ams_service.get_roles("user123")
    mock_get.assert_called_once_with("user123/roles")


@patch.object(AccountManagementService, 'put')
def test_update_roles(mock_put, ams_service):
    roles = ["admin", "user"]
    ams_service.update_roles("user123", roles)
    mock_put.assert_called_once_with("user123/roles", data={"roles": roles})


@patch.object(AccountManagementService, 'get')
def test_has_role(mock_get, ams_service):
    ams_service.has_role("user123", "admin")
    mock_get.assert_called_once_with("user123/has-role/admin")


@patch.object(AccountManagementService, 'get')
def test_get_permissions(mock_get, ams_service):
    ams_service.get_permissions("user123")
    mock_get.assert_called_once_with("user123/permissions")


@patch.object(AccountManagementService, 'put')
def test_update_permissions(mock_put, ams_service):
    permissions = ["read", "write"]
    ams_service.update_permissions("user123", permissions)
    mock_put.assert_called_once_with("user123/permissions", data={"permissions": permissions})


@patch.object(AccountManagementService, 'get')
def test_has_permission(mock_get, ams_service):
    ams_service.has_permission("user123", "read")
    mock_get.assert_called_once_with("user123/has-permission/read")


@patch.object(AccountManagementService, 'get')
def test_get_groups(mock_get, ams_service):
    ams_service.get_groups("user123")
    mock_get.assert_called_once_with("user123/groups")


@patch.object(AccountManagementService, 'put')
def test_update_groups(mock_put, ams_service):
    groups = ["group1", "group2"]
    ams_service.update_groups("user123", groups)
    mock_put.assert_called_once_with("user123/groups", data={"groups": groups})


@patch.object(AccountManagementService, 'get')
def test_has_group(mock_get, ams_service):
    ams_service.has_group("user123", "group1")
    mock_get.assert_called_once_with("user123/has-group/group1")


@patch.object(AccountManagementService, 'get')
def test_get_offices(mock_get, ams_service):
    ams_service.get_offices("user123")
    mock_get.assert_called_once_with("user123/offices")


@patch.object(AccountManagementService, 'put')
def test_update_offices(mock_put, ams_service):
    offices = ["office1", "office2"]
    ams_service.update_offices("user123", offices)
    mock_put.assert_called_once_with("user123/offices", data={"offices": offices})


@patch.object(AccountManagementService, 'get')
def test_has_office(mock_get, ams_service):
    ams_service.has_office("user123", "office1")
    mock_get.assert_called_once_with("user123/has-office/office1")


@patch.object(AccountManagementService, 'get')
def test_get_all_users(mock_get, ams_service):
    ams_service.get_all_users(page=2, per_page=30)
    mock_get.assert_called_once_with("users", params={"page": 2, "per_page": 30})


@patch.object(AccountManagementService, 'get')
def test_search_users(mock_get, ams_service):
    ams_service.search_users("John")
    mock_get.assert_called_once_with("users/search", params={"q": "John"})


@patch.object(AccountManagementService, 'get')
def test_search_users_by_email(mock_get, ams_service):
    ams_service.search_users_by_email("john@example.com")
    mock_get.assert_called_once_with("users/search-by-email", params={"email": "john@example.com"})
