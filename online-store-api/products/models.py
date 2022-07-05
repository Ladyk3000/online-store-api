from django.db import models

# Create your models here.
class Category(models.Model):
	Category_Id = models.AutoField(primary_key = True)
	Category_Parent_Id = models.IntegerField()
	Category_Name = models.ChatField(max_length = 100)

class Product(model.Model):
	Product_Category_Id = models.AutoField(primary_key = True)
	Product_Name = models.CharField(max_length = 100)
	Product_VendorCode = models.CharField(max_length = 100)
	Product_Code = models.AutoField()
	Product_Description  = models.CharField(max_length = 500)

class Offer(models.Model):
	Offer_Price = models.FloatField()
	Offer_Id = models.AutoField(primary_key = True)
	Offer_Price_begin  = models.FloatField()
	Offer_size = models.IntegerField()
	Offer_model = models.AutoField()


