from django.urls import URLPattern, path
from . import views

urlpatterns =[
    path('cartDetails', views.cart_details, name='cartDetails'),
    path('add/<int:product_id>/', views.add_cart, name='addcart'),
    # path('decrement/<int:product_id>/', views.minus_cart, name='cart_decrement'), or
    path('cart_decrement/<int:product_id>/', views.minus_cart, name='cart_decrement'),

    # path('delete/<int:product_id>/', views.cart_delete, name='remove'),  or
    path('remove/<int:product_id>/', views.cart_delete, name='remove'),


]