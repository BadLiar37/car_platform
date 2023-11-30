from rest_framework import status, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenViewBase

from apps.user.models import User, Passport
from apps.user.serializers import (
    UserSerializer,
    UserTokenSerializer,
    PassportSerializer,
)

from core.permissions import IsOwnerOnly, IsCurrentUserOrAdminOnly


class PassportViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    """
    Only registered users can create passport data and only owners can view and modify passport data.

    retrieve: Retrieve passport by id

    update: Update passport by id

    create: Create new passport data

    partial_update: Patch passport by id
    """

    permission_classes = (IsOwnerOnly,)
    serializer_class = PassportSerializer

    # users can only access their passport
    def get_queryset(self):
        queryset = Passport.objects.filter(user_id=self.request.user.id)
        return queryset

    # adding user ID to the serializer before creating a passport object
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    """
    Users can register, modify and delete their own accounts. Admin users can modify and delete data of all users

    retrieve: Retrieve user by id

    update: Update user by id

    create: Create new user

    partial_update: Patch user by id

    delete: Delete user by id
    """

    permission_classes = (IsCurrentUserOrAdminOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):
        # check if this is a partial update or not
        partial = kwargs.pop("partial", False)
        # retrieve an object from a database
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        instance.set_password(serializer.data.get("password"))
        instance.save()
        return Response(serializer.data)


class LoginView(TokenViewBase):
    """
    View to authenticate and obtain an access token
    """

    serializer_class = UserTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            raise ValueError(f"Verification Failure: {e}")
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
