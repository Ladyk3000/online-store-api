from rest_framework import serializers
from products.models import Category, Product, Offer

class CategorySerializer(serializers.ModelSerializer):
	model = Categories
	fields = ('Category_Id','Category_Parent_Id','Category_Name')

class ProductSerializer(serializers.ModelSerializer):
	model = Products
	fields = ('Product_Model','Product_Name','Product_Category_Id','Product_VendorCode','Product_Description')

class OfferSerializer(serializers.ModelSerializer):
	model = Offers
	fields = ('Offer_Price','Offer_Id','Offer_Price_begin','Offer_size','Offer_model')	
