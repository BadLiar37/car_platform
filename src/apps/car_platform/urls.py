from django.urls import include, path
from rest_framework import routers

from apps.car_platform.views import CarViewSet, FeatureViewSet

router = routers.SimpleRouter()

router.register(r"cars", CarViewSet, basename="car")
router.register(r"features", FeatureViewSet, basename="feature")

urlpatterns = [
    path("", include(router.urls)),
]
