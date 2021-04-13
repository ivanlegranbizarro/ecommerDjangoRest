from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


# Create your views here.

class LatestProductsList(generics.ListAPIView):
    queryset = Product.objects.all()[0:4]
    serializer_class = ProductSerializer


class SearchProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    lookup_field = 'slug'
    serializer_class = CategorySerializer
