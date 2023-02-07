from django.urls import path
from .views import CategoryListAPIView, ProductCreateAPIView, ProductUpdateAPIView, FavoriteAPIView, ProductDestroyAPIView, ProductListAPIView, OrderAPIView


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('product_create/', ProductCreateAPIView.as_view()),
    path('favorite/', FavoriteAPIView.as_view()),
    path('update-product/<int:pk>', ProductUpdateAPIView.as_view()),
    path('delete-product/<int:pk>', ProductDestroyAPIView.as_view()),
    path('product_list/', ProductListAPIView.as_view()),

]