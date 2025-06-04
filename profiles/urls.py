from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, SubscriptionViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'subscriptions', SubscriptionViewSet, basename='subscription')

urlpatterns = [
    path('', include(router.urls)),

    path('users/<int:pk>/subscribe/',
         SubscriptionViewSet.as_view({'post': 'create', 'delete': 'destroy'}),
         name='user-subscribe'),
]