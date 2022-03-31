from rest_framework import serializers
from .models import Pizza

class CartSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = [
      "id",
      "imageUrl",
      "name",
      "types",
      "sizes",
      "price",
      "category",
      "rating"]