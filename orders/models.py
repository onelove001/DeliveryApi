from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    SIZE = (("XL", "xl"), ("LA", "la"), ("ME", "me"), ("SM", "sm"),)
    ORDER_STATUS = ( ("PENDING", "pending"), ("IN_TRANSIT", "in_transit"), ("DELIVERED", "delivered"), )
    size = models.CharField(max_length=20, choices=SIZE, default=SIZE[3][0])
    status = models.CharField(max_length = 20, choices=ORDER_STATUS, default=[0][0])
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.user.email} - {self.size}"
