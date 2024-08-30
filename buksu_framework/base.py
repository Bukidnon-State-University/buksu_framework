from buksu_framework.api_client import StandardAPIClient
from buksu_framework.mixins import BaseMixin


class BaseService(StandardAPIClient, BaseMixin):
    __test__ = False

    def __init__(self, realm, access_token, version=None):
        super().__init__(realm, access_token, self.service, version=version or self.version)
