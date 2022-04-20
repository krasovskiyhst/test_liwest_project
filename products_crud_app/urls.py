from products_crud_app.views import CategoriesOfProductsViewSet, GroupsOfProductsViewSet, ProductsViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('api/v1/product-categories', CategoriesOfProductsViewSet)
router.register('api/v1/product-groups', GroupsOfProductsViewSet)
router.register('api/v1/products', ProductsViewSet)
urlpatterns = router.urls
