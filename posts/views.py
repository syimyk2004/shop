from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView


from .serializers import CategorySerializers
from .models import Category



class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers