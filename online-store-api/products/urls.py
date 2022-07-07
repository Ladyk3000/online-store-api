from django.urls import path
from . import views

urlpatterns = [
 path('', views.fill_db),
 path('products/<int:id>', views.get_products),
 path('product/<int:id>', views.get_product)
]