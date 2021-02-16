from .models import Product
from .serializers import ProductSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser


def products_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(data=serializer.data, safe=False)

    #if request.method == 'POST':