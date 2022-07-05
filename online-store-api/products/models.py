from django.db import models

# Create your models here.
class Category(models.Model):
	Category_Id = models.AutoField(primary_key = True)
	Category_Parent_Id = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
	Category_Name = models.ChatField(max_length = 100)

class Product(model.Model):
	Product_Model = models.AutoField(primary_key = True)
	Product_Name = models.CharField(max_length = 100)
	Product_Category_Id = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
	Product_VendorCode = models.CharField(max_length = 100)
	Product_Description = models.CharField(max_length = 500)

class Offer(models.Model):
	Offer_Price = models.FloatField()
	Offer_Id = models.AutoField(primary_key = True)
	Offer_Price_begin  = models.FloatField()
	Offer_size = models.IntegerField()
	Offer_model = models.ForeignKey('Product')


