from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models import User


class TrustMeBroAuthentication(BaseAuthentication):
    def authenticate(self, request):
        name = request.headers.get("Trust-Me")
        if not name:
            return None
        try:
            user = User.objects.get(name=name)
            return (user, None)
        except User.DoesNotExist:
            raise AuthenticationFailed(f"No user {name}")
