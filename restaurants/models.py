from django.db import models


# 餐廳資料表
class Restaurants(models.Model):
    class Meta:
        verbose_name = '餐廳'

    name = models.CharField(max_length=50, verbose_name='餐廳名稱')
    address = models.CharField(max_length=100, verbose_name='餐廳地址')
    food_types = models.CharField(max_length=50, verbose_name='餐廳類型')
    visit_time = models.DateField()
    purpose = models.CharField(max_length=10, verbose_name='造訪目的')
    short_comment = models.CharField(max_length=255, verbose_name='短評')
