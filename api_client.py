import requests


class APIClientBase:

    def __init__(self, realm, access_token, base_url):
        self.realm = realm
        self.access_token = access_token
        self.base_url = base_url.rstrip('/')

    def get_authorization(self):
        return f"Bearer realm:{self.realm} {self.access_token}"

    def request(self, method, endpoint, data=None, params=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        headers = {
            "Authorization": self.get_authorization(),
            "Content-Type": "application/json"
        }

        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            json=data,
            params=params
        )

        response.raise_for_status()
        return response.json()

    def get(self, endpoint, params=None):
        return self.request("GET", endpoint, params=params)

    def post(self, endpoint, data=None):
        return self.request("POST", endpoint, data=data)

    def put(self, endpoint, data=None):
        return self.request("PUT", endpoint, data=data)

    def delete(self, endpoint, params=None):
        return self.request("DELETE", endpoint, params=params)


class StandardAPIClient(APIClientBase):
    def __init__(self, realm, access_token, service, version="v1"):
        super().__init__(realm, access_token, "https://api.buksu.edu.ph")
        self.service = service
        self.version = version

    def _format_endpoint(self, method_or_endpoint):
        return f"/{self.service}/{self.version}/{method_or_endpoint.lstrip('/')}"

    def get(self, method_or_endpoint, params=None):
        return super().get(self._format_endpoint(method_or_endpoint), params=params)

    def post(self, method_or_endpoint, data=None):
        return super().post(self._format_endpoint(method_or_endpoint), data=data)

    def put(self, method_or_endpoint, data=None):
        return super().put(self._format_endpoint(method_or_endpoint), data=data)

    def delete(self, method_or_endpoint, params=None):
        return super().delete(self._format_endpoint(method_or_endpoint), params=params)
