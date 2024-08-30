from buksu_framework.base import BaseService
from buksu_framework.mixins import BaseMixin


class AccountManagementService(BaseService, BaseMixin):
    """
    Account Management Service

    This class provides methods to interact with the account management API
    using the standard endpoint format: /ams/{version}/
    """

    service = "ams"

    # User Registration and Profile Management
    def register_user(self, data):
        """
        Register a new user.

        Args:
            data (dict): User registration data.

        Returns:
            dict: Response containing the registered user's information.
        """
        return self.post("register", data=data)

    def profile(self, user_id):
        """
        Get user profile information.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict: User profile information.
        """
        return self.get(f"{user_id}/profile")
    
    def update_profile(self, user_id, data):
        """
        Update user profile information.

        Args:
            user_id (str): The ID of the user.
            data (dict): Updated profile data.

        Returns:
            dict: Updated user profile information.
        """
        return self.put(f"{user_id}/profile", data=data)
    
    def get_user_by_email(self, email):
        """
        Get user information by email address.

        Args:
            email (str): The email address of the user.

        Returns:
            dict: User information.
        """
        return self.get(f"user-by-email/{email}")

    # Password Management
    def change_password(self, user_id, data):
        """
        Change user's password.

        Args:
            user_id (str): The ID of the user.
            data (dict): Password change data (old and new password).

        Returns:
            dict: Response indicating success or failure.
        """
        return self.put(f"{user_id}/change-password", data=data)

    # Social Account Management
    def get_social_accounts(self, user_id):
        """
        Get social accounts associated with a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            list: List of social accounts associated with the user.
        """
        return self.get(f"{user_id}/social-accounts")
    
    def add_social_account(self, user_id, data):
        """
        Add a social account to a user.

        Args:
            user_id (str): The ID of the user.
            data (dict): Social account data.

        Returns:
            dict: Response indicating success or failure.
        """
        return self.post(f"{user_id}/social-accounts", data=data)
    
    def remove_social_account(self, user_id, provider):
        """
        Remove a social account from a user.

        Args:
            user_id (str): The ID of the user.
            provider (str): The provider of the social account.

        Returns:
            dict: Response indicating success or failure.
        """
        return self.delete(f"{user_id}/social-accounts/{provider}")

    # OTP Management
    def verify_otp(self, user_id, otp):
        """
        Verify OTP for a user.

        Args:
            user_id (str): The ID of the user.
            otp (str): The OTP to verify.

        Returns:
            dict: Response indicating success or failure.
        """
        return self.post(f"{user_id}/verify-otp", data={"otp": otp})
    
    def setup_otp(self, user_id):
        """
        Setup OTP for a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict: Response indicating success or failure.
        """
        return self.post(f"{user_id}/setup-otp")
    
    def remove_otp(self, user_id):
        """
        Remove OTP for a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict: Response indicating success or failure.
        """
        return self.delete(f"{user_id}/otp")

    # Account Status Management
    def activate_user(self, user_id):
        """
        Activate a user account.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict: Response indicating success or failure.
        """
        return self.put(f"{user_id}/activate")
    
    def deactivate_user(self, user_id):
        """
        Deactivate a user account.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict: Response indicating success or failure.
        """
        return self.put(f"{user_id}/deactivate")
    
    def delete_account(self, user_id):
        """
        Delete a user account.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict: Response indicating success or failure.
        """
        return self.delete(f"{user_id}")

    # Role Management
    def get_roles(self, user_id):
        """
        Get roles assigned to a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            list: List of roles assigned to the user.
        """
        return self.get(f"{user_id}/roles")
    
    def update_roles(self, user_id, roles):
        """
        Update roles assigned to a user.

        Args:
            user_id (str): The ID of the user.
            roles (list): List of role IDs to assign to the user.

        Returns:
            dict: Updated list of roles assigned to the user.
        """
        return self.put(f"{user_id}/roles", data={"roles": roles})
    
    def has_role(self, user_id, role):
        """
        Check if a user has a specific role.

        Args:
            user_id (str): The ID of the user.
            role (str): The role to check.

        Returns:
            bool: True if the user has the role, False otherwise.
        """
        return self.get(f"{user_id}/has-role/{role}")

    # Permission Management
    def get_permissions(self, user_id):
        """
        Get permissions assigned to a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            list: List of permissions assigned to the user.
        """
        return self.get(f"{user_id}/permissions")
    
    def update_permissions(self, user_id, permissions):
        """
        Update permissions assigned to a user.

        Args:
            user_id (str): The ID of the user.
            permissions (list): List of permission IDs to assign to the user.

        Returns:
            dict: Updated list of permissions assigned to the user.
        """
        return self.put(f"{user_id}/permissions", data={"permissions": permissions})
    
    def has_permission(self, user_id, permission):
        """
        Check if a user has a specific permission.

        Args:
            user_id (str): The ID of the user.
            permission (str): The permission to check.

        Returns:
            bool: True if the user has the permission, False otherwise.
        """
        return self.get(f"{user_id}/has-permission/{permission}")

    # Group Management
    def get_groups(self, user_id):
        """
        Get groups a user belongs to.

        Args:
            user_id (str): The ID of the user.

        Returns:
            list: List of groups the user belongs to.
        """
        return self.get(f"{user_id}/groups")
    
    def update_groups(self, user_id, groups):
        """
        Update groups a user belongs to.

        Args:
            user_id (str): The ID of the user.
            groups (list): List of group IDs to assign to the user.

        Returns:
            dict: Updated list of groups the user belongs to.
        """
        return self.put(f"{user_id}/groups", data={"groups": groups})
    
    def has_group(self, user_id, group):
        """
        Check if a user belongs to a specific group.

        Args:
            user_id (str): The ID of the user.
            group (str): The group to check.

        Returns:
            bool: True if the user belongs to the group, False otherwise.
        """
        return self.get(f"{user_id}/has-group/{group}")

    # Office Management
    def get_offices(self, user_id):
        """
        Get offices associated with a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            list: List of offices associated with the user.
        """
        return self.get(f"{user_id}/offices")
    
    def update_offices(self, user_id, offices):
        """
        Update offices associated with a user.

        Args:
            user_id (str): The ID of the user.
            offices (list): List of office IDs to associate with the user.

        Returns:
            dict: Updated list of offices associated with the user.
        """
        return self.put(f"{user_id}/offices", data={"offices": offices})
    
    def has_office(self, user_id, office):
        """
        Check if a user is associated with a specific office.

        Args:
            user_id (str): The ID of the user.
            office (str): The office to check.

        Returns:
            bool: True if the user is associated with the office, False otherwise.
        """
        return self.get(f"{user_id}/has-office/{office}")

    # User Listing and Search
    def get_all_users(self, page=1, per_page=20):
        """
        Get a paginated list of all users.

        Args:
            page (int, optional): The page number to retrieve. Defaults to 1.
            per_page (int, optional): The number of users per page. Defaults to 20.

        Returns:
            dict: Paginated list of users.
        """
        return self.get("users", params={"page": page, "per_page": per_page})
    
    def search_users(self, query):
        """
        Search for users based on a query string.

        Args:
            query (str): The search query.

        Returns:
            list: List of users matching the search query.
        """
        return self.get("users/search", params={"q": query})
    
    def search_users_by_email(self, email):
        """
        Search for users by email address.

        Args:
            email (str): The email address to search for.

        Returns:
            list: List of users matching the email address.
        """
        return self.get("users/search-by-email", params={"email": email})