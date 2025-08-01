from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse  # 👈 add this import
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Poll API",
      default_version='v1',
      description="API documentation for the Poll System",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# 👇 add this simple root view
def root_view(request):
    return JsonResponse({"message": "Welcome to the Poll API"})

urlpatterns = [
    path('', root_view),  # 👈 handles /
    path('admin/', admin.site.urls),
    path('api/', include('polls.urls')),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
