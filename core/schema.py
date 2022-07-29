import graphene
#import graphql_jwt
from apps.categories.schema import(
    CategoryQuery,
    CreateCategoryMutation,
    UpdateCategoryMutation,
    DeleteCategoryMutation
)

from apps.questions.schema import (
    QuestionQuery
)

from apps.quizzes.schema import (
    QuizQuery
)

from apps.answers.schema import (
    AnswerQuery
)



class Query(CategoryQuery, QuizQuery, QuestionQuery, AnswerQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    # category mutation
    create_category = CreateCategoryMutation.Field()
    update_category = UpdateCategoryMutation.Field()
    delete_category = DeleteCategoryMutation.Field()

    # # auth mutation
    # token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    # verify_token = graphql_jwt.Verify.Field()
    # refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)