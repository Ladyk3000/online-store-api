from rest_framework import serializers
from products.models import Category, Product, Offer

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('id', 'category_name','parent_id')

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('product_name','product_description','product_category','product_brand','product_article')

class OfferSerializer(serializers.ModelSerializer):
	class Meta:
		model = Offer
		fields = ('offer_product','offer_price','offer_price_begin','offer_available','offer_size')	
