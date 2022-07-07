from unicodedata import category
from django.http import HttpResponse, JsonResponse
from .models import Category, CategoryRelation, Product, Offer
from .serializers import CategorySerializer, ProductSerializer, OfferSerializer
import xmltodict
PATH = "/app/test_catalog.xml"

'''
def categoriesApi(request):
	if request.method == 'GET':
		categories = Categories.objects.all()
		categories_serializer = CategorySerializer(categories, many = True)
		return JsonResponse(categories_serializer.data, safe = False)
	elif request.method == 'POST':
		categories_data = JSONParser().parse(request)
		categories_serializer = CategorySerializer(data = categories_data)
		if categories_serializer.is_valid():
			categories_serializer.save()
			return JsonResponse("save successfully")
		return JsonResponse("fail", safe = False)
'''
def get_products(request, id):
	if request.method == 'POST': #!!!!!!!!!!!!!!!!!!
		category = Category.objects.filter(id = id)
		categoryserializer = CategorySerializer(category, many = True)
		return JsonResponse(categoryserializer.data, safe = False, json_dumps_params={'ensure_ascii': False})
	return JsonResponse(f"failed to load category id: {id}", safe = False)

def get_product(request, id):
	if request.method == 'GET':
		product = Product.objects.filter(id = id)
		productserializer = ProductSerializer(product, many = True)

		offer = Offer.objects.filter(offer_product_id = id)
		offerserializer = OfferSerializer(offer, many = True)

		return JsonResponse(productserializer.data + offerserializer.data, safe = False, json_dumps_params={'ensure_ascii': False})
	return JsonResponse(f"failed to load product id: {id}", safe = False)

def fill_db(request):
	with open(PATH, encoding='utf-8') as fd:
		doc = xmltodict.parse(fd.read(), dict_constructor=dict)

	for item in doc['yml_catalog']['shop']['categories']['category']:
		try:
			category = Category(category_name = item['#text'], id=item['@id'], parent_id=item['@parentId'])
		except KeyError:
			category = Category(category_name = item['#text'], id=item['@id'], parent_id='000000001')
		category.save()
		# print(item)
		# if item['@parentId']:
		# 	categoryrelation = CategoryRelation(category_parent = item['@parentId'], category_child = item['@id'])
		# 	categoryrelation.save()

	for item in doc['yml_catalog']['shop']['offers']['offer']:
		print(item)

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

	return HttpResponse(f"All data has been entered into the database")