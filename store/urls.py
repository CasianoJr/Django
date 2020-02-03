from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_all, name='product-all'),
    path('product/<slug>/', views.product_detail, name='product-detail'),
    path('search/', views.store_search, name='store-search'),
    path('cart/', views.cart, name='store-cart'),
]
