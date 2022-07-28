import graphene
from graphql import GraphQLError
from .models import Category
from graphene_django import DjangoObjectType


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryQuery(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)
    category_detail = graphene.Field(CategoryType, category_id=graphene.ID())

    def resolve_all_categories(self,  info, **kwargs):
        return Category.objects.all()

    def resolve_category_detail(self, info, category_id, **kwargs):
        return Category.objects.get(id=category_id)


class CategoryInput(graphene.InputObjectType):
    name = graphene.String()

    def __str__(self):
        return self.name


class CreateCategoryMutation(graphene.Mutation):
    class Arguments:
        input = CategoryInput(required=True)

    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root, info, input):
        if not Category.objects.filter(name__icontains=input.name).exists():
            instance = Category(
                name = input.name
            )
            instance.save()
            return CreateCategoryMutation(category=instance)
        raise GraphQLError("this category already exist")


class UpdateCategoryMutation(graphene.Mutation):
    class Arguments:
        input = CategoryInput(required=True)

    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root, info, input):
        instance = Category.objects.get(id=input.id)
        if instance:
            instance.name = input.name
            instance.save()
            return UpdateCategoryMutation(category=instance)
        return UpdateCategoryMutation(category=None)


class DeleteCategoryMutation(graphene.Mutation):
    class Arguments:
        category_id = graphene.ID()

    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root, info, category_id):
        instance = Category.objects.get(id=category_id)
        if instance:
            instance.delete()
            return DeleteCategoryMutation(category=None)
        return GraphQLError("Item not found...")