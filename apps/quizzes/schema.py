import graphene
from .models import Quiz
from graphene_django import DjangoObjectType


class QuizType(DjangoObjectType):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuizQuery(graphene.ObjectType):
    all_quizzes = graphene.List(QuizType)
    quiz_detail = graphene.Field(QuizType, quiz_id=graphene.ID())

    def resolve_all_quizzes(root, info, **kwargs):
        return Quiz.objects.all()

    def resolve_quiz_detail(root, info, quiz_id, **kwargs):
        return Quiz.objects.get(id=quiz_id)