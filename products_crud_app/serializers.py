from rest_framework import serializers

from products_crud_app.models import CategoriesOfProduct, GroupsOfProduct, Product


class CategoriesOfProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesOfProduct
        fields = '__all__'


class GroupsOfProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupsOfProduct
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
