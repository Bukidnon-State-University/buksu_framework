from unittest.mock import patch, Mock

import pytest

from buksu_framework.api_client import APIClientBase, StandardAPIClient


@pytest.fixture
def base_client():
    return APIClientBase("test_realm", "test_token", "https://api.example.com")


@pytest.fixture
def standard_client():
    return StandardAPIClient("test_realm", "test_token", "test_service")


def test_get_authorization(base_client):
    assert base_client.get_authorization() == "Bearer realm:test_realm test_token"


@patch('requests.request')
def test_request_method(mock_request, base_client):
    mock_response = Mock()
    mock_response.json.return_value = {"key": "value"}
    mock_request.return_value = mock_response

    result = base_client.request("GET", "test_endpoint", params={"param": "value"})

    mock_request.assert_called_once_with(
        method="GET",
        url="https://api.example.com/test_endpoint",
        headers={
            "Authorization": "Bearer realm:test_realm test_token",
            "Content-Type": "application/json"
        },
        json=None,
        params={"param": "value"}
    )
    assert result == {"key": "value"}


def test_http_methods(base_client):
    methods = ["get", "post", "put", "delete"]
    for method in methods:
        with patch.object(base_client, 'request') as mock_request:
            getattr(base_client, method)("test_endpoint")
            if method in ["post", "put"]:
                mock_request.assert_called_once_with(method.upper(), "test_endpoint", data=None)
            else:
                mock_request.assert_called_once_with(method.upper(), "test_endpoint", params=None)


def test_standard_client_init(standard_client):
    assert standard_client.base_url == "https://api.buksu.edu.ph"
    assert standard_client.service == "test_service"
    assert standard_client.version == "v1"


def test_standard_client_format_endpoint(standard_client):
    assert standard_client._format_endpoint("method") == "/test_service/v1/method"
    assert standard_client._format_endpoint("/method") == "/test_service/v1/method"


@patch.object(APIClientBase, 'get')
def test_standard_client_get(mock_get, standard_client):
    standard_client.get("test_method", params={"param": "value"})
    mock_get.assert_called_once_with("/test_service/v1/test_method", params={"param": "value"})


@patch.object(APIClientBase, 'post')
def test_standard_client_post(mock_post, standard_client):
    standard_client.post("test_method", data={"key": "value"})
    mock_post.assert_called_once_with("/test_service/v1/test_method", data={"key": "value"})


@patch.object(APIClientBase, 'put')
def test_standard_client_put(mock_put, standard_client):
    standard_client.put("test_method", data={"key": "updated_value"})
    mock_put.assert_called_once_with("/test_service/v1/test_method", data={"key": "updated_value"})


@patch.object(APIClientBase, 'delete')
def test_standard_client_delete(mock_delete, standard_client):
    standard_client.delete("test_method")
    mock_delete.assert_called_once_with("/test_service/v1/test_method", params=None)


def test_standard_client_all_methods_format_endpoint(standard_client):
    methods = ['get', 'post', 'put', 'delete']
    for method in methods:
        with patch.object(APIClientBase, method) as mock_method:
            getattr(standard_client, method)("test_method")
            if method in ["post", "put"]:
                mock_method.assert_called_once_with("/test_service/v1/test_method", data=None)
            else:
                mock_method.assert_called_once_with("/test_service/v1/test_method", params=None)


def test_standard_client_custom_version():
    custom_client = StandardAPIClient("test_realm", "test_token", "test_service", version="v2")
    assert custom_client.version == "v2"
    assert custom_client._format_endpoint("method") == "/test_service/v2/method"

# Similar tests can be added for post, put, and delete methods of StandardAPIClient
