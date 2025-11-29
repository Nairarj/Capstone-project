from rest_framework import serializers
from .models import menu, booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = ['id', 'title', 'price', 'inventory']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = '__all__'