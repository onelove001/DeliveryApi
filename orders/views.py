from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from .models import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model


User = get_user_model()


class OrderCreateList(generics.GenericAPIView):
    serializer_class = serializers.OrderCreationSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        orders = Order.objects.all()
        serializer = self.serializer_class(instance = orders, many=True)
        return Response(data = serializer.data, status=status.HTTP_200_OK)



    def post(self, request):
        user = request.user
        user = User.objects.get(email = user)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(user=user)

            return Response(data = serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,  status = status.HTTP_400_BAD_REQUEST)


class OrderDetailedView(generics.GenericAPIView):
    serializer_class = serializers.OrderUpdatedSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, order_id):
        order = get_object_or_404(Order, pk = order_id)
        serializer = self.serializer_class(instance = order)
        return Response(data = serializer.data, status=status.HTTP_200_OK)


    def put(self, request, order_id):
        data = request.data
        order = get_object_or_404(Order, pk = order_id)
        serializer = self.serializer_class(data = data, instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors,  status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request, order_id):
        order = get_object_or_404(Order, pk = order_id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateStatusView(generics.GenericAPIView):
    serializer_class = serializers.OrderStatusUpdatedSerializer

    def put(self, request, order_id):
        data = request.data
        order = get_object_or_404(Order, pk = order_id)
        serializer = self.serializer_class(data = data, instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors,  status = status.HTTP_400_BAD_REQUEST)


class UserOrderView(generics.GenericAPIView):
    serializer_class = serializers.OrderUpdatedSerializer

    def get(self, request, user_id):
        user = User.objects.get(pk = user_id)

        orders = Order.objects.filter(user = user)
        serializer = self.serializer_class(instance = orders, many=True)
        return Response(data = serializer.data, status=status.HTTP_200_OK) 


class UserOrderDetail(generics.GenericAPIView):
    serializer_class = serializers.OrderStatusUpdatedSerializer

    def get(self, request, user_id, order_id):
        user = User.objects.get(pk = user_id)
        try: 
            Order.objects.filter(user = user).get(pk=order_id).exists()
            print("Exists")
            Order.objects.filter(user = user).get(pk=order_id)
            serializer = self.serializer_class(instance = order, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)