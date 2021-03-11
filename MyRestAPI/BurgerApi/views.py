from rest_framework.viewsets import ModelViewSet

# Create your views here.
from .models import UserProfile
from BurgerApi.serializers import UserProfileSerializer


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
