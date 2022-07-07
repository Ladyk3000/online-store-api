from django.http import HttpResponse
from .models import Category, CategoryRelation, Product, Offer

import xmltodict
PATH = "/app/test_catalog.xml"

'''
@csrf_exempt
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

def test(request):
	return HttpResponse("test")

def fill_test(request):
	with open(PATH, encoding='utf-8') as fd:
		doc = xmltodict.parse(fd.read(), dict_constructor=dict)

	for item in doc['yml_catalog']['shop']['categories']['category']:
		print(item)
		try:
			print('no parent')
			category = Category(category_name = item['#text'], id=item['@id'], parent_id=item['@parentId'])
		except KeyError:
			print('parent')
			category = Category(category_name = item['#text'], id=item['@id'], parent_id='000000001')
		category.save()
		# print(item)
		# if item['@parentId']:
		# 	categoryrelation = CategoryRelation(category_parent = item['@parentId'], category_child = item['@id'])
		# 	categoryrelation.save()

	for item in doc['yml_catalog']['shop']['offers']['offer']:
		product = Product(product_name = item['name'], product_description = item['description'], product_category_id=item['categoryId'])
		product.save()

		offer = Offer(offer_description="100 rubley beri jinsy!", offer_product=product, offer_price=item['price'])
		offer.save()

	return HttpResponse(f"Category {category.id}")