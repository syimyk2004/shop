from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter
from .serializers import CategorySerializers, ProductSerializers, FavoriteSerializers, OrderSerializers
from .models import Category, Product, Favorite, Order, Order_product
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet





class IsOwnerOrAdmin(permissions.BasePermission):
    """Класс разрешений для владельца объекта"""
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.creator == request.user

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class FavoriteAPIView(APIView):
    def post(self, request):
        user = request.user
        data = request.data
        data["user"] = user.id
        serializer = FavoriteSerializers(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers



class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [SearchFilter]
    search_fields = ['price', 'name', 'quntity', 'description']
     




class OrderAPIView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

    