from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title="Django apps",
        default_version="v1",
        description="Car_platform",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="myemail@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/car_platform/", include("apps.car_platform.urls")),
    path("api/v1/users/", include("apps.user.urls")),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # urls for swagger API
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
