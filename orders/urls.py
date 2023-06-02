from django.urls import path
from  .views import *

app_name="order"

urlpatterns = [
    path("", OrderCreateList.as_view(), name="orders"),
]