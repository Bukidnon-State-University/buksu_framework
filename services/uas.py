from buksu_framework.base import BaseService

class UserAuthService(BaseService):
    """
    User Authentication Service
    """
    
    service_name = "uas"

    # Registration and login
    def register(self, email, password, params={}):
        """
        Register a user
        """
        return self.post("register", data={"email": email, "password": password, **params})

    def login(self, email, password):
        """
        Login a user
        """
        return self.post("login", data={"email": email, "password": password})
    
    def logout(self, token):
        """
        Logout a user
        """
        return self.post("logout", data={"token": token})
    
    # OTP Management
    def verify_otp(self, email, otp):
        """
        Verify OTP
        """
        return self.post("verify-otp", data={"email": email, "otp": otp})
    
    def verify_email(self, email, token):
        """
        Verify Email
        """
        return self.post("verify-email", data={"email": email, "token": token})
    
    # Social Authentication
    def social_register(self, provider, token):
        """
        Social Register
        """
        return self.post("social-register", data={"provider": provider, "token": token})
    
    def social_login(self, provider, token):
        """
        Social Login
        """
        return self.post("social-login", data={"provider": provider, "token": token})
    
    # Password Management
    def forgot_password(self, email):
        """
        Forgot Password
        """
        return self.post("forgot-password", data={"email": email})

    def reset_password(self, email, password, token):
        """
        Reset Password
        """
        return self.post("reset-password", data={"email": email, "password": password, "token": token})
    
    def change_password(self, email, password, new_password):
        """
        Change Password
        """
        return self.post("change-password", data={"email": email, "password": password, "new_password": new_password})
    
    # Token Management
    def refresh_token(self, token):
        """
        Refresh Token
        """
        return self.post("refresh-token", data={"token": token})
    
    def get_access_token(self, refresh_token):
        """
        Get Access Token
        """
        return self.post("access-token", data={"token": refresh_token})

