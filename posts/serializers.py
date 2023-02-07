from rest_framework import serializers

from .models import Category, Product, Favorite, Order, Order_product, Item
from django.contrib.auth import get_user_model

User = get_user_model()


class CategorySerializers(serializers.ModelSerializer):

    
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
class FavoriteSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(required=False, queryset=User.objects.all())
    class Meta:
        model = Favorite
        fields = "__all__"

class OrderSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(required=False, queryset=User.objects.all())
    class Meta:
        model = Order
        fields = "__all__"

    

        

class Order_productSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order_product
        fields = '__all__'
