from django.urls import path, include

from store import views

urlpatterns = [
    path('products/', views.ProductsListView.as_view()),
    path('products/search/', views.SearchView),
    path('checkout/', views.checkout),
    path('orders/', views.OrdersList.as_view()),
    path("orders/<pk>",views.order_delete),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),

]
