from django.urls import path
from  .views import *

app_name="order"

urlpatterns = [
    path("", OrderCreateList.as_view(), name="orders"),
    path("<int:order_id>", OrderDetailedView.as_view(), name="order-object"),
    path("update-status/<int:order_id>", UpdateStatusView.as_view(), name="status-object"),
    path("user/<int:user_id>/orders", UserOrderView.as_view(), name="user-orders"),
    path("user/<int:user_id>/orders/<int:order_id>", UserOrderDetail.as_view(), name="user-specific-details"),
]