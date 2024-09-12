from django.urls import path

from . import views


urlpatterns = [
    path('home', views.home),
    path('authorized', views.authorized),
    path('products/<int:pk>', views.product_detail),
    path('products', views.list_prod)
]
