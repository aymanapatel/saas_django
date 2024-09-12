from django.urls import path

from . import views


urlpatterns = [
    # Functional Based View URL Config
    # path('home', views.home),
    # path('authorized', views.authorized),
    # Class Based View URL Config
    path('home', views.HomeView.as_view()),
    path('authorized', views.AuthorizedView.as_view()),
    path('products/<int:pk>', views.product_detail),
    path('products', views.list_prod)
]
