from rest_framework import viewsets
from .models import CustomUser, Subscription
from .serializers import CustomUserSerializer, SubscriptionSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
