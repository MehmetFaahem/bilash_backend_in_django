from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from core.views import ProductViewSet, CustomerViewSet  # Add your CustomerViewSet

# Initialize the router
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'customers', CustomerViewSet)  # Register your CustomerViewSet

# Setup the schema view for Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="My Admin Panel API",
        default_version='v1',
        description="API documentation for My Admin Panel",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myadminpanel.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

