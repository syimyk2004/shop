from rest_framework import serializers

from .models import Category, Product, Favorite, Order, Order_product


class CategorySerializers(serializers.ModelSerializer):

    
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerialzers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
class FavoriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class Order_productSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order_product
        fields = '__all__'
