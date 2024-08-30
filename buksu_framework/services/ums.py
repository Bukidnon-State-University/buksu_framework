from buksu_framework.base import BaseService
from buksu_framework.mixins import CRUDMixin


class UserMediaService(BaseService, CRUDMixin):
    """
    User Media Service

    This class provides methods to interact with the user media API
    using the standard endpoint format: /ums/{version}/
    """

    service = "ums"
    global_params = {"storage": "local"}

    def update(self, media_id, data=None, params=None):
        return super().update(media_id, data=data, params=params)
