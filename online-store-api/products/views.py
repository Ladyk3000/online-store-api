from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.responce import JsonResponse

from products.models import Category, Product, Offer
from products.serializers imoport CategorySerializer, ProductSerializer, OfferSerializer
# Create your views here.

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