from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Restaurants
from .serializers import RestaurantsSerializer


# 創建餐廳資料
class RestaurantsCreate(generics.CreateAPIView):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer


# 顯示所有餐廳資料
class RestaurantsList(generics.ListCreateAPIView):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


# 修改餐廳資料
class RestaurantsUpdate(generics.RetrieveUpdateAPIView):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


# 刪除餐廳資料
class RestaurantsDelete(generics.DestroyAPIView):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'
