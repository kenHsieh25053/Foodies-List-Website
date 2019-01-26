from .views import RestaurantsCreate, RestaurantsList, RestaurantsUpdate, RestaurantsDelete

from django.urls import path


urlpatterns = [
    # 創建餐廳資料API
    path('restaurants/create/', RestaurantsCreate.as_view(), name="res-create"),
    # 顯示餐廳資料API
    path('restaurants/list/',
         RestaurantsList.as_view(), name="res-list"),
    path('restaurants/list/<int:pk>/',
         RestaurantsList.as_view(), name="res-list-single"),
    # 更新餐廳資料API
    path('restaurants/update/<int:pk>/',
         RestaurantsUpdate.as_view(), name="res-update"),
    # 刪除餐廳資料API
    path('restaurants/delete/<int:pk>/',
         RestaurantsDelete.as_view(), name="res-delete")
]
