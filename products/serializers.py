from rest_framework import serializers
from products.models import Category, Product, Offer


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('id', 'category_name', 'parent_id')


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
	class Meta:
		model = Offer
		fields = '__all__'
