from django.urls import include, path
from rest_framework import routers

from apps.user.views import (
    UserViewSet,
    LoginView,
    PassportViewSet,
)

router = routers.SimpleRouter()

router.register("user", UserViewSet, basename="user")
router.register("passport", PassportViewSet, basename="passport")

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("", include(router.urls)),
]
