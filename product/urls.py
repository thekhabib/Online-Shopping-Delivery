from django.urls import path

from product.views import CategoryListCreateView, ProductListCreateView, ProductDetailView, \
    DeliveryListCreateView, DeliveryDetailView, ProductItemListCreateView, ProductItemDetailView, \
    GetProductItemListView, SortBenefitListView


urlpatterns = [
    path('product/', ProductListCreateView.as_view(), name='product_list_create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/', CategoryListCreateView.as_view(), name='category_list_create'),
    path('delivery/', DeliveryListCreateView.as_view(), name='delivery_list_create'),
    path('delivery/<int:pk>/', DeliveryDetailView.as_view(), name='delivery_detail'),
    path('product-item/', ProductItemListCreateView.as_view(), name='product_item_list_create'),
    path('product-item/<int:pk>/', ProductItemDetailView.as_view(), name='product_item_detail'),
    path('get-product/', GetProductItemListView.as_view(), name='get_product_list'),
    path('max-benefits/', SortBenefitListView.as_view(), name='sort_benefit_list'),
]

