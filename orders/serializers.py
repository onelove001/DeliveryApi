from .models import *
from rest_framework import serializers




class OrderCreationSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20)
    status = serializers.HiddenField(default="PENDING")
    quantity = serializers.IntegerField()


    class Meta:
        model = Order
        fields = ["size", "status", "quantity"]
