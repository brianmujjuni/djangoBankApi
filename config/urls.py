from django.conf import settings
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

 
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/schema", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/vi/schema/swagger-ui",
        SpectacularSwaggerView.as_view(url_name="schema"),
    ),
    path("api/v1/schema/redoc",SpectacularRedocView.as_view(url_name="schema"),name="redoc")
]

admin.site.site_header = "Automex Bank Admin"
admin.site.site_title = "Automex Bank Admin Portal"
admin.site.index_title = "Welcome to Automex Bank Admin Portal"
