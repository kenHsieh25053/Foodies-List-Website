from rest_framework import serializers
from .models import Restaurants


class RestaurantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = (
            'id', 'name', 'address', 'food_types', 'visit_time', 'purpose', 'short_comment')
