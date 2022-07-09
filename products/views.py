from unicodedata import category
from django.http import HttpResponse, JsonResponse
from .models import Category, CategoryRelation, Product, Offer
from .serializers import CategorySerializer, ProductSerializer, OfferSerializer
import xmltodict
from rest_framework.generics import ListCreateAPIView, ListCreateAPIView
from rest_framework import permissions

PATH = "/app/media/test_catalog.xml"

class CategoryAPIView(ListCreateAPIView):

	def post(self, request, id):
		category = Category.objects.filter(id = id)
		categoryserializer = CategorySerializer(category, many = True)

		product = Product.objects.filter(product_category_id = id)
		productserializer = ProductSerializer(product, many=True)

		response = {'category': categoryserializer.data, 'products': productserializer.data}
		return JsonResponse(response, safe = False, json_dumps_params={'ensure_ascii': False})


	def get(self, request, id):	
		product = Product.objects.filter(id = id)
		productserializer = ProductSerializer(product, many=True)

		offer = Offer.objects.filter(offer_product_id = id)
		offerserializer = OfferSerializer(offer, many = True)
		response = {'product': productserializer.data, 'offers': offerserializer.data}
		return JsonResponse(response, safe = False, json_dumps_params={'ensure_ascii': False})


class Fill_Database(ListCreateAPIView):

	def get(self, request):
		with open(PATH, encoding='utf-8') as fd:
			doc = xmltodict.parse(fd.read(), dict_constructor=dict)

		for item in doc['yml_catalog']['shop']['categories']['category']:
			try:
				category = Category(category_name = item['#text'], id=item['@id'], parent_id=item['@parentId'])
			except KeyError:
				category = Category(category_name = item['#text'], id=item['@id'], parent_id='000000001')
			category.save()

		for item in doc['yml_catalog']['shop']['offers']['offer']:

			product = Product(
				product_name = item['name'], 
				product_description = item['description'], 
				product_category_id = item['categoryId'], 
				product_brand = item['param'][0]['#text'],
				product_article = item['param'][1]['#text']
				)
			product.save()

			offer = Offer(
				offer_product=product,
				offer_price=item['price'],
				offer_price_begin=item['price_begin'],
				offer_available=item['@available']
				)
			try:
				offer.offer_size = item['param'][2]['#text']
			except KeyError:
				offer.offer_size = '0'
			offer.save()

		return HttpResponse(f"All data has been entered into the database go to http://127.0.0.1:8000/swagger")
