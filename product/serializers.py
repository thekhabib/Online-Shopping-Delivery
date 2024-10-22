from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from product.models import Category, Product, Delivery, ProductItem


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'


class PostProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Delivery
        fields = '__all__'


class ProductItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    product = ProductSerializer()
    deliver = DeliverySerializer()

    class Meta:
        model = ProductItem
        fields = '__all__'


class PostProductItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    deliver = serializers.PrimaryKeyRelatedField(queryset=Delivery.objects.all())

    class Meta:
        model = ProductItem
        fields = '__all__'

