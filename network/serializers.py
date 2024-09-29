from rest_framework import serializers
from .models import NetworkNode


class NetworkNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        fields = ['id', 'name', 'email', 'country', 'city', 'street', 'house_number', 'product_name', 'product_model', 'product_release_date', 'supplier', 'debt', 'level', 'created_at']
        read_only_fields = ['debt']
