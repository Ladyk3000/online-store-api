from unicodedata import category
from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True, editable=True)
    parent_id = models.IntegerField()


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=200)
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='product_category')
    product_photos = models.TextField()
    product_brand = models.CharField(max_length=200)
    product_article = models.CharField(max_length=200)
    product_color = models.CharField(max_length=20)
    product_vendor_color = models.CharField(max_length=20)
    product_upper_material = models.CharField(max_length=200)
    product_lining_material = models.CharField(max_length=200)
    product_sole_material = models.CharField(max_length=200)
    product_heel_height = models.IntegerField()
    product_sole_height = models.IntegerField()
    product_sex = models.CharField(max_length=10)
    product_type = models.CharField(max_length=20)
    product_season = models.CharField(max_length=20)
    product_sale_season = models.CharField(max_length=20)
    product_style = models.CharField(max_length=20)
    product_style_Region = models.CharField(max_length=30)
    product_manufacturer_Region = models.CharField(max_length=30)
    product_weight = models.IntegerField()
    product_length = models.IntegerField()
    product_width = models.IntegerField()
    product_height = models.IntegerField()
    product_insole_material = models.CharField(max_length=30)


class Offer(models.Model):
    offer_product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='offer_product')
    offer_price = models.IntegerField()
    offer_price_begin = models.IntegerField()
    offer_percent = models.IntegerField()
    offer_size = models.IntegerField()
    offer_RU_size = models.IntegerField()
    offer_available = models.CharField(max_length=10)
    offer_vendor_code = models.CharField(max_length=20)
    offer_vat = models.IntegerField()
