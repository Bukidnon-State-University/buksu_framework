BukSU Framework API Documentation
=================================

Table of Contents
-----------------

*   [Installation](#installation)
*   [Getting Started](#getting-started)
*   Services
    *   [Account Management Service (AMS)](#ams)
    *   [User Authentication Service (UAS)](#uas)
    *   [User Media Service (UMS)](#ums)
    *   [Global Notification Service (GNS)](#gns)
    *   [Organization Data Service (ODS)](#ods)

Installation
------------

To install the BukSU Framework, use pip:

    pip install buksu_framework

Getting Started
---------------

To use the BukSU Framework, you need to import the required services and initialize them with your realm and access token.

    from buksu_framework.services.ams import AccountManagementService
    from buksu_framework.services.uas import UserAuthService
    from buksu_framework.services.ums import UserMediaService
    from buksu_framework.services.gns import GlobalNotificationService
    from buksu_framework.services.ods import OrganizationDataService
    
    # Initialize services
    realm = "your_realm"
    access_token = "your_access_token"
    
    ams = AccountManagementService(realm, access_token)
    uas = UserAuthService(realm, access_token)
    ums = UserMediaService(realm, access_token)
    gns = GlobalNotificationService(realm, access_token)
    ods = OrganizationDataService(realm, access_token)
    

Account Management Service (AMS)
--------------------------------

The Account Management Service provides methods for managing user accounts, profiles, roles, and permissions.

### Key Methods

*   register\_user(data): Register a new user
*   profile(user\_id): Get user profile information
*   update\_profile(user\_id, data): Update user profile information
*   change\_password(user\_id, data): Change user's password
*   get\_roles(user\_id): Get roles assigned to a user
*   update\_roles(user\_id, roles): Update roles assigned to a user
*   get\_permissions(user\_id): Get permissions assigned to a user
*   update\_permissions(user\_id, permissions): Update permissions assigned to a user

### Example Usage

    # Register a new user
    user_data = {"username": "newuser", "email": "newuser@example.com", "password": "securepassword"}
    result = ams.register_user(user_data)
    
    # Get user profile
    profile = ams.profile("user123")
    
    # Update user profile
    update_data = {"name": "John Doe", "bio": "Software Developer"}
    updated_profile = ams.update_profile("user123", update_data)
    
    # Change password
    password_data = {"old_password": "oldpassword", "new_password": "newpassword"}
    ams.change_password("user123", password_data)
    
    # Update user roles
    new_roles = ["admin", "editor"]
    ams.update_roles("user123", new_roles)
    

User Authentication Service (UAS)
---------------------------------

The User Authentication Service handles user authentication, including login, logout, and token management.

### Key Methods

*   register(email, password, params={}): Register a new user
*   login(email, password): Login a user
*   logout(token): Logout a user
*   verify\_otp(email, otp): Verify OTP
*   social\_login(provider, token): Social login
*   forgot\_password(email): Initiate forgot password process
*   reset\_password(email, password, token): Reset password
*   refresh\_token(token): Refresh authentication token

### Example Usage

    # Login
    login_result = uas.login("user@example.com", "password123")
    
    # Logout
    uas.logout(login_result["token"])
    
    # Social login
    social_login_result = uas.social_login("google", "google_token_123")
    
    # Forgot password
    uas.forgot_password("user@example.com")
    
    # Reset password
    uas.reset_password("user@example.com", "newpassword123", "reset_token_123")
    
    # Refresh token
    new_token = uas.refresh_token("old_token_123")
    

User Media Service (UMS)
------------------------

The User Media Service manages user media files, such as profile pictures or document uploads.

### Key Methods

*   list(params=None): List user media files
*   create(data): Upload a new media file
*   retrieve(id): Get details of a specific media file
*   update(id, data): Update media file details
*   remove(id): Delete a media file

### Example Usage

    # List media files
    media_list = ums.list(params={"page": 1, "per_page": 20})
    
    # Upload a new media file
    media_data = {"file_name": "profile.jpg", "file_type": "image/jpeg", "file_content": "base64_encoded_content"}
    new_media = ums.create(media_data)
    
    # Get media file details
    media_details = ums.retrieve("media123")
    
    # Update media file details
    update_data = {"file_name": "new_profile.jpg"}
    updated_media = ums.update("media123", update_data)
    
    # Delete a media file
    ums.remove("media123")
    

Global Notification Service (GNS)
---------------------------------

The Global Notification Service manages notifications for users and groups.

### Key Methods

*   list(params=None): List notifications
*   retrieve(id): Get details of a specific notification
*   read(id): Mark a notification as read
*   unread(id): Mark a notification as unread
*   mark\_all\_as\_read(): Mark all notifications as read
*   mark\_all\_as\_unread(): Mark all notifications as unread
*   notify(user\_id, data): Send a notification to a user
*   notify\_group(group\_id, data): Send a notification to a group
*   notify\_all(data): Send a notification to all users

### Example Usage

    # List notifications
    notifications = gns.list(params={"page": 1, "per_page": 20})
    
    # Get notification details
    notification_details = gns.retrieve("notification123")
    
    # Mark notification as read
    gns.read("notification123")
    
    # Send notification to a user
    notification_data = {"message": "New message received", "type": "message"}
    gns.notify("user123", notification_data)
    
    # Send notification to a group
    group_notification_data = {"message": "Team meeting reminder", "type": "reminder"}
    gns.notify_group("group123", group_notification_data)
    
    # Send notification to all users
    global_notification_data = {"message": "System maintenance scheduled", "type": "system"}
    gns.notify_all(global_notification_data)
    

Organization Data Service (ODS)
-------------------------------

The Organization Data Service manages data related to organizational units and offices.

### Key Methods

*   list(params=None): List organizational units/offices
*   create(data): Create a new organizational unit/office
*   retrieve(id): Get details of a specific organizational unit/office
*   update(id, data): Update details of an organizational unit/office
*   remove(id): Delete an organizational unit/office

### Example Usage

    # List organizational units/offices
    org_units = ods.list(params={"page": 1, "per_page": 20})
    
    # Create a new organizational unit/office
    org_unit_data = {"name": "New Office", "location": "Main Campus"}
    new_org_unit = ods.create(org_unit_data)
    
    # Get organizational unit/office details
    org_unit_details = ods.retrieve("org_unit123")
    
    # Update organizational unit/office details
    update_data = {"name": "Updated Office Name"}
    updated_org_unit = ods.update("org_unit123", update_data)
    
    # Delete an organizational unit/office
    ods.remove("org_unit123")