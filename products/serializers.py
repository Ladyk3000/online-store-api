from rest_framework import serializers
from products.models import Category, Product, Offer


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('id', 'category_name','parent_id')

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('product_name','product_description','product_category','product_brand','product_article',
				'product_color','product_vendor_color','product_upper_material','product_lining_material',
				'product_sole_material','product_heel_height','product_sole_height','product_sex','product_type',
				'product_season','product_sale_season','product_style','product_style_Region','product_manufacturer_Region',
				'product_weight','product_length','product_width','product_height','product_insole_material')

class OfferSerializer(serializers.ModelSerializer):
	class Meta:
		model = Offer
		fields = ('offer_product','offer_price','offer_percent', 'offer_price_begin','offer_available',
				'offer_size','offer_RU_size','offer_vendor_code','offer_vat')	
