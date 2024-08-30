from buksu_framework.base import BaseService
from buksu_framework.mixins import CRUDMixin


class OrganizationDataService(BaseService, CRUDMixin):
    """
    Organization Data Service

    This class provides methods to interact with the units/offices API
    using the standard endpoint format: /units/{version}/
    """

    service = "ods"
