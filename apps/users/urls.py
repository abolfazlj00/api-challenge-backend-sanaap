# apps/users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRoleViewSet, LoginAPIView

router = DefaultRouter()
router.register(r'', UserRoleViewSet, basename='user-role')

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('', include(router.urls)),
]
