from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.
from . models import (Customer,Product,Cart,Order)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','locations','city','zipcode','state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','discunted_prce','discription',
    'brand','Category','product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quentity']

@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','product_info','customer','customer_info','quentity','order_date','status']
    
    def customer_info(self,obj):
        link = reverse("admin:ecomm_customer_change",args=[obj.
        customer.pk])
        return format_html('<a href="{}">{}</>', link , obj.customer.name)
    
    def product_info(self,obj):
        link = reverse("admin:ecomm_product_change",args=[obj.
        product.pk])
        return format_html('<a href="{}">{}</>', link , obj.product.title)