from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import PayViewSet

app_name = UsersConfig.name


router = DefaultRouter()
router.register(r'pay', PayViewSet, basename='pay')

urlpatterns = [

] + router.urls
