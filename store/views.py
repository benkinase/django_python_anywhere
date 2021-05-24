from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import HttpResponse
import stripe

from django.conf import settings
from django.contrib.auth.models import User

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Product, Category,Order
from .serializers import ProductSerializer, CategorySerializer,OrderSerializer, MyOrderSerializer

def index(request):
    return HttpResponse(
    """
    <div>
    <h1>Welcome</h1>
       <a class="admin" href='/admin/'>GO TO ADMIN</a>
    </div>
    """)

# HANDLE PRODUCT LISTING
class ProductsListView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):

        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


# HANDLE PRODUCT DETAIL
class ProductDetail(APIView):
    permission_classes = (permissions.AllowAny,)
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


# HANDLE CATEGORY
class CategoryDetail(APIView):
    permission_classes = (permissions.AllowAny,)
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


# HANDLE PRODUCT SEARCH
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def SearchView(request):

    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        if serializer.is_valid:
            return Response(serializer.data)
        else:
            return Response(serializer.errors,{"message":f"No match found for {query}!"})
    else:
        return Response({"products": [], "message":"No match found!"})


# HANDLE CHECKOUT/PAYMENT
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():

        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])

        try:
            stripe.Charge.create(
                amount=int(paid_amount * 100),
                currency='USD',
                description='Charge from Redflower GmbH',
                source=serializer.validated_data['stripe_token']
            )

            serializer.save(user=request.user, paid_amount=paid_amount)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# HANDLE USER ORDER LISTING
class OrdersList(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)


# HANDLE SINGLE ORDER REMOVAL
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def order_delete(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({'message': 'The order does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method=="DELETE":
        order.delete()
        return Response({'message': 'Order was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



