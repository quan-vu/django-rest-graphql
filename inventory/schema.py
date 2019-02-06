import graphene

from graphene_django.types import DjangoObjectType

from .models import Product

class ProductType(DjangoObjectType):
    class Meta:
        model = Product


# Create an abstract query: a subclass of AbstractType
class Query(graphene.AbstractType):
    all_products = graphene.List(ProductType)
    product = graphene.Field(ProductType, id=graphene.Argument(graphene.Int, required=True))

    def resolve_all_products(self, context, **kwargs):
        return Product.objects.all()

    def resolve_product(self, context, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Product.objects.get(pk=id)

        return None