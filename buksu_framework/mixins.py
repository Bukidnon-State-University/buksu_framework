# pylint: disable=too-few-public-methods
class BaseMixin:
    """
    Base Mixin

    This class is a mixin for all services utilizing standard API endpoints.
    """

    service = None
    version = "v1"
    global_params = {}

    class Meta:
        abstract = True

    def __init__(self, realm, access_token, service, version=None):
        self.realm = realm
        self.access_token = access_token
        self.service = service
        self.version = version or "v1"

    def get_service_info(self):
        """Return basic service information."""
        return {
            "service": self.service,
            "version": self.version,
            "realm": self.realm
        }


class ListMixin(BaseMixin):
    """
    List Mixin

    This class is a mixin for all services utilizing standard API endpoints.
    """

    def list(self, params=None):
        merged_params = {**self.global_params, **(params or {})}
        return self.get("", params=merged_params)


class CreateMixin(BaseMixin):
    """
    Create Mixin

    This class is a mixin for all services utilizing standard API endpoints.
    """

    def create(self, data, params=None):
        merged_params = {**self.global_params, **(params or {})}
        return self.post("", data=data, params=merged_params)


class RetrieveMixin(BaseMixin):
    """
    Retrieve Mixin

    This class is a mixin for all services utilizing standard API endpoints.
    """

    def retrieve(self, item_id, params=None):
        merged_params = {**self.global_params, **(params or {})}
        return self.get(item_id, params=merged_params)


class UpdateMixin(BaseMixin):
    """
    Update Mixin

    This class is a mixin for all services utilizing standard API endpoints.
    """

    def update(self, item_id, data=None, params=None):
        merged_params = {**self.global_params, **(params or {})}
        return self.put(item_id, data=data, params=merged_params)


class DeleteMixin(BaseMixin):
    """
    Delete Mixin

    This class is a mixin for all services utilizing standard API endpoints.
    """

    def remove(self, item_id, params=None):
        merged_params = {**self.global_params, **(params or {})}
        return self.delete(item_id, params=merged_params)


class CRUDMixin(ListMixin, CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin):
    """
    CRUD Mixin

    This class is a mixin for all services utilizing standard API endpoints.
    """
