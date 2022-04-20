from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from products_crud_app.models import CategoriesOfProduct, GroupsOfProduct, Product
from products_crud_app.serializers import CategoriesOfProductsSerializer, GroupsOfProductsSerializer, ProductsSerializer

from django.db.models.deletion import ProtectedError


class Return400IfProtectedErrorViewSet(viewsets.ModelViewSet):
    """ Класс от которого унаследованы "Категории" и "Группы" """

    def destroy(self, request, *args, **kwargs):
        """ Попытка удаления, при котором возвращается 400, если есть зависимые сущности """
        instance = self.get_object()
        try:
            self.perform_destroy(instance)
        except ProtectedError as exception:
            content = {'exception': str(exception)}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoriesOfProductsViewSet(Return400IfProtectedErrorViewSet):
    queryset = CategoriesOfProduct.objects.all()
    serializer_class = CategoriesOfProductsSerializer


class GroupsOfProductsViewSet(Return400IfProtectedErrorViewSet):
    queryset = GroupsOfProduct.objects.all()
    serializer_class = GroupsOfProductsSerializer

    def get_queryset(self):
        lookup_url_kwargs_categories_id = self.request.query_params.get("categories_id")
        if lookup_url_kwargs_categories_id:
            self.queryset = self.queryset.filter(category_id=lookup_url_kwargs_categories_id)

        return self.queryset


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(hidden=False)
    serializer_class = ProductsSerializer

    def get_queryset(self):
        lookup_url_kwargs_search_by_name = self.request.query_params.get("search_by_name")
        lookup_url_kwargs_group_id = self.request.query_params.get("group_id")
        if lookup_url_kwargs_search_by_name:
            self.queryset = self.queryset.filter(name=lookup_url_kwargs_search_by_name)

        if lookup_url_kwargs_group_id:
            self.queryset = self.queryset.filter(group_id=lookup_url_kwargs_group_id)

        return self.queryset
