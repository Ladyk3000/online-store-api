from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
 path('upload_data/', views.FileUploadView.as_view()),
 path('products/<int:id>', views.CategoryAPIView.as_view()),
 path('product/<int:id>', views.ProductAPIView.as_view())
]
