from django.contrib import admin

from .models import Category, Product, Order,OrderItem

class ProductAdmin(admin.ModelAdmin):
    list_display= ('id',"name",'price',"size", "color",)
    list_filter=("name", "price","color",)
    prepopulated_fields={"slug":("name",)}


admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
