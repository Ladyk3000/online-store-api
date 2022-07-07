from unicodedata import category
from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True, editable=True)
    parent_id = models.IntegerField()

class CategoryRelation(models.Model):
    category_parent = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category_parent')
    category_child = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category_child')

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=200)
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='product_category')
    product_brand = models.CharField(max_length=200)
    product_article = models.CharField(max_length=200)
    #product_picture = models.ImageField() #???????

class Offer(models.Model):
    offer_product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='offer_product')
    offer_price = models.IntegerField()
    offer_price_begin = models.IntegerField()
    offer_size = models.IntegerField()
    offer_available = models.CharField(max_length=200)#BooleanField()
