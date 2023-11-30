from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import viewsets

from apps.car_platform.models import Car, Feature
from apps.car_platform.serializers import CarSerializer, FeatureSerializer
from core.permissions import IsOwnerElseReadOnly, IsAdminOrReadOnly


class FeatureViewSet(viewsets.ModelViewSet):
    """
    Admin users can create, modify and delete features, the other users can only view them

    list: Returns a list of features

    retrieve: Retrieve feature by id

    update: Update feature by id

    create: Create new feature

    partial_update: Patch feature by id

    delete: Delete feature by id
    """

    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = (IsAdminOrReadOnly,)

    # caching requests for 1 hour
    @method_decorator(cache_page(60 * 60 * 1))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        data = super().list(request, *args, **kwargs)
        return data


class CarViewSet(viewsets.ModelViewSet):
    """
    Only car owners can modify and delete cars, registered users can create and view cars,
    anonymous users can only view them.

    list: Returns a list of cars

    retrieve: Retrieve car by id

    update: Update car by id

    create: Create new car

    partial_update: Patch car by id

    delete: Delete car by id
    """

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsOwnerElseReadOnly,)

    # adding an owner ID to the serializer before creating a car object
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @method_decorator(cache_page(60 * 60 * 1))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        data = super().list(request, *args, **kwargs)
        return data
