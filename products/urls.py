from django.urls import path
from . import views

urlpatterns = [
 path('load_data/', views.Fill_Database.as_view()),
 path('products/<int:id>', views.CategoryAPIView.as_view()),
 path('product/<int:id>', views.CategoryAPIView.as_view())
]