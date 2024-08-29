from buksu_framework.base import BaseService
from buksu_framework.mixins import ListMixin, RetrieveMixin, CRUDMixin

class GlobalNotificationService(BaseService, CRUDMixin):
    """
    Global Notification Service

    This class provides methods to interact with the global notifications API
    using the standard endpoint format: /gns/{version}/
    """

    service = "gns"
    global_params = {}  # Add this line

    def read(self, id):
        return self.post(f"{id}/read")
    
    def unread(self, id):
        return self.post(f"{id}/unread")
    
    def mark_all_as_read(self):
        return self.post("mark-all-as-read")
    
    def mark_all_as_unread(self):
        return self.post("mark-all-as-unread")
    
    def notify(self, user_id, data):
        return self.post(f"{user_id}/notify", data=data)
    
    def notify_group(self, group_id, data):
        return self.post(f"{group_id}/notify", data=data)
    
    def notify_all(self, data):
        return self.post("notify-all", data=data)


