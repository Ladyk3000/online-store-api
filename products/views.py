from unicodedata import category
from django.http import HttpResponse, JsonResponse
from .models import Category, Product, Offer
from .serializers import CategorySerializer, ProductSerializer, OfferSerializer
import xmltodict
from rest_framework.generics import ListCreateAPIView, ListAPIView
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from rest_framework.views import APIView

PATH = "/app/media/test_catalog.xml"


class FileUploadView(ListCreateAPIView):
	def get(self, request):
		return render(request, 'upload.html')

	def post(self, request):
		uploaded_file = request.FILES['xml_data']
		fs = FileSystemStorage()
		fs.save(uploaded_file.name, uploaded_file)
		self.upload_data()
		return HttpResponse("File uploaded")
		
	def upload_data(self):
		with open(PATH, encoding='utf-8') as fd:
			doc = xmltodict.parse(fd.read(), dict_constructor=dict)

		for item in doc['yml_catalog']['shop']['categories']['category']:
			try:
				category = Category(category_name=item['#text'], 
									id=item['@id'], parent_id=item['@parentId'])
			except KeyError:
				category = Category(category_name=item['#text'], 
									id=item['@id'], parent_id='000000001')
			category.save()

		for item in doc['yml_catalog']['shop']['offers']['offer']:
			product = Product(
				product_name = item['name'], 
				product_description = item['description'], 
				product_category_id = item['categoryId'],
				product_photos = ', '.join(item['picture']),
				product_brand = item['param'][0]['#text'],
				product_article = item['param'][1]['#text'],
				product_color = item['param'][4]['#text'],
				product_vendor_color = item['param'][5]['#text'],
				product_sex = item['param'][11]['#text'],
				product_type = item['param'][12]['#text'],
				product_season = item['param'][13]['#text'],
				product_sale_season = item['param'][14]['#text'],
				product_style = item['param'][15]['#text'],
				product_style_Region =item['param'][16]['#text'],
				product_manufacturer_Region =item['param'][17]['#text'],
				product_weight = item['param'][18]['#text'],
				product_length = item['param'][19]['#text'],
				product_width = item['param'][20]['#text'],
				product_height = item['param'][21]['#text'],
				)
			
			try:
				product.product_upper_material = item['param'][6]['#text']
				product.product_lining_material = item['param'][7]['#text']
				product.product_sole_material = item['param'][8]['#text']
				product.product_heel_height = item['param'][9]['#text']
				product.product_sole_height = item['param'][10]['#text']
				product.product_insole_material = item['param'][22]['#text']
				
			except KeyError:
				product.product_upper_material = 'none'
				product.product_lining_material = 'none'
				product.product_sole_material = 'none'
				product.product_heel_height =  '0'
				product.product_sole_height =  '0'
				product.product_insole_material = 'none'
			product.save()

			offer = Offer(
				offer_product=product,
				offer_price=item['price'],
				offer_price_begin=item['price_begin'],
				offer_available=item['@available'],
				offer_vat=item['vat'],
				offer_vendor_code=item['vendorCode'],
				offer_percent=item['percent']
				)
			try:
				offer.offer_RU_size = item['param'][2]['#text']
				offer.offer_size = item['param'][3]['#text']
			except KeyError:
				offer.offer_RU_size = '0'
				offer.offer_size = '0'
			offer.save()

		return HttpResponse(f"All data has been entered into the database")

	
class CategoryAPIView(ListAPIView):
	def post(self, request, id):
		category = Category.objects.filter(id = id)
		categoryserializer = CategorySerializer(category, many = True)

		product = Product.objects.filter(product_category_id = id)
		productserializer = ProductSerializer(product, many=True)

		response = {'category': categoryserializer.data, 'products': productserializer.data}
		return JsonResponse(response, json_dumps_params={'ensure_ascii': False})


class ProductAPIView(ListAPIView):
	def get(self, request, id):	
		product = Product.objects.filter(id = id)
		productserializer = ProductSerializer(product, many=True)

		offer = Offer.objects.filter(offer_product_id = id)
		offerserializer = OfferSerializer(offer, many = True)
		response = {'product': productserializer.data, 'offers': offerserializer.data}
		return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
		