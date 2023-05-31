from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response


class orderView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message": "Hello Order View"}, status=status.HTTP_200_OK)


