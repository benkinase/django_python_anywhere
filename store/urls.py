from django.urls import path, include

from store import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/products/', views.ProductsListView.as_view()),
    path('api/products/search/', views.SearchView),
    path('api/checkout/', views.checkout),
    path('api/orders/', views.OrdersList.as_view()),
    path("api/orders/<pk>",views.order_delete),
    path('api/products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('api/products/<slug:category_slug>/', views.CategoryDetail.as_view()),

]
