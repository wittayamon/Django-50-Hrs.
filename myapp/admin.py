from django.contrib import admin
from myapp.models import Tracking, Product, askQA

class ManageProduct(admin.ModelAdmin):
    list_display=["name","price","stock","description","trendingnow"]
    list_editable=["price","stock","description","trendingnow"]
    list_per_page=5
    search_fields=["name"]
    list_filter=["trendingnow"]

# Register your models here.
admin.site.register(Tracking)
admin.site.register(askQA)
admin.site.register(Product,ManageProduct) # admin.site.register(Model, Class) รับอากิวเมนต์เข้ามาเพิ่มอีก 1 ตัวคือ Class ในที่นี้คือ ManageProduct