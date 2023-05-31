from django.urls import path
from  .views import *

app_name="order"

urlpatterns = [
    path("", orderView.as_view(), name="order-view"),
]