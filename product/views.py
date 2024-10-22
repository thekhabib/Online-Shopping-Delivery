from django.contrib.admin.templatetags.admin_list import results
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product, Category, ProductItem, Delivery
from product.serializers import CategorySerializer, ProductSerializer, DeliverySerializer, ProductItemSerializer, \
    PostProductSerializer, PostProductItemSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostProductSerializer
        return ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return PostProductSerializer
        return ProductSerializer


class DeliveryListCreateView(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class DeliveryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class ProductItemListCreateView(generics.ListCreateAPIView):
    queryset = ProductItem.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostProductItemSerializer
        return ProductItemSerializer


class ProductItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductItem.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return PostProductItemSerializer
        return ProductItemSerializer


class GetProductItemListView(APIView):

    def post(self, request, *args, **kwargs):
        product = request.data['product']
        product = get_object_or_404(Product, name=product)
        product_list = []
        for prod in ProductItem.objects.filter(product=product):
            if prod.quantity > 0:
                prod = ProductItemSerializer(prod).data
                product_list.append(prod)

        return Response(product_list)


class SortBenefitListView(APIView):

    def get(self, request, *args, **kwargs):
        prod_list = ProductItem.objects.all()
        benefits = dict()
        for prod in prod_list:
            elem = prod.product.name
            if elem in benefits:
                benefits[elem] += prod.quantity * prod.base_price
            else:
                benefits[elem] = prod.quantity * prod.base_price
        benefits = dict(sorted(benefits.items(), key=lambda item: item[1], reverse=True))
        results = []
        for key in benefits:
            prod = get_object_or_404(Product, name=key)
            results.append(
                {
                    'product_id': prod.id,
                    'product_name': prod.name,
                    'benefit': benefits[key],
                }
            )
        print(results)
        return Response(results)

