
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("authentication.urls", namespace="auth")),
    path("orders/", include("orders.urls", namespace="order")),
    path("auth/", include("djoser.urls.jwt")),
]
