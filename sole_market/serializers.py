from rest_framework import serializers

from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            # "category",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail",
        ]


class CategorySerializer(serializers.ModelSerializer):
    products_within = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ["id", "name", "get_absolute_url", "products_within"]
        depth = 2
