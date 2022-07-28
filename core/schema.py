import graphene
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
    create_category = CreateCategoryMutation.Field()
    update_category = UpdateCategoryMutation.Field()
    delete_category = DeleteCategoryMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)