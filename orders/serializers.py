from rest_framework import serializers
from .models import Food

class FoodSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=64)
    priceSmall = serializers.FloatField()
    priceLarge = serializers.FloatField()
    quantity = serializers.IntegerField()
    specialInstructions = serializers.CharField(max_length=640)
    menu = serializers.BooleanField()
    status = serializers.CharField(max_length=64)
    user_id = serializers.IntegerField()

    def create(self, validated_data):
        return Food.objects.create(**validated_data)
