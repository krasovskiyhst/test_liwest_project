from django.contrib import admin
from .models import CategoriesOfProduct, GroupsOfProduct, Product

admin.site.register(Product)


@admin.register(GroupsOfProduct)
class GroupsOfProduct(admin.ModelAdmin):
    list_display = ("name", "description", "seq")


@admin.register(CategoriesOfProduct)
class CategoriesOfProduct(admin.ModelAdmin):
    list_display = ("name", "seq")
