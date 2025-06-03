from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MealViewSet, ComponentViewSet, LabelViewSet

router = DefaultRouter()
router.register('meals', MealViewSet)
router.register('components', ComponentViewSet)
router.register('labels', LabelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]