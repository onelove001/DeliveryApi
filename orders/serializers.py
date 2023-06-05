from .models import *
from rest_framework import serializers


class OrderCreationSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20)
    status = serializers.CharField(default="PENDING")
    quantity = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ["id", "size", "status", "quantity", "created_at"]



class OrderUpdatedSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20)
    status = serializers.CharField(default="PENDING")
    quantity = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ["id", "size", "status", "quantity", "updated_at"]



class OrderStatusUpdatedSerializer(serializers.ModelSerializer):
    status = serializers.CharField(default="PENDING")

    class Meta:
        model = Order
        fields = ["status", "updated_at"]