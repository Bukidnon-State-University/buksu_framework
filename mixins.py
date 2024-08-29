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

    def retrieve(self, id, params=None):
        merged_params = {**self.global_params, **(params or {})}
        return self.get(id, params=merged_params)


class UpdateMixin(BaseMixin):
    """
    Update Mixin

    This class is a mixin for all services utilizing standard API endpoints.
    """

    def update(self, id, data=None, params=None):
        merged_params = {**self.global_params, **(params or {})}
        return self.put(id, data=data, params=merged_params)


class DeleteMixin(BaseMixin):
    """
    Delete Mixin

    This class is a mixin for all services utilizing standard API endpoints.
    """

    def remove(self, id, params=None):
        merged_params = {**self.global_params, **(params or {})}
        return self.delete(id, params=merged_params)


class CRUDMixin(ListMixin, CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin):
    """
    CRUD Mixin

    This class is a mixin for all services utilizing standard API endpoints.
    """
