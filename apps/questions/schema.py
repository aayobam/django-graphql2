import graphene
from .models import Question
from graphene_django import DjangoObjectType


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionQuery(graphene.ObjectType):
    all_questions = graphene.List(QuestionType)
    question_detail = graphene.Field(QuestionType, question_id=graphene.ID())

    def resolve_all_questions(root, info, **kwargs):
        return Question.objects.all()

    def resolve_question_detail(root, info, question_id, **kwargs):
        return Question.objects.get(id=question_id)