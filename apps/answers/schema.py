import graphene
from .models import Answer
from graphene_django import DjangoObjectType


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = '__all__'


class AnswerQuery(graphene.ObjectType):
    all_answers = graphene.List(AnswerType)
    answer_detail = graphene.Field(AnswerType, answer_id=graphene.ID())

    def resolve_all_answers(root, info, **kwargs):
        return Answer.objects.all()

    def resolve_answer_detail(root, info, answer_id, **kwargs):
        return Answer.objects.get(id=answer_id)


class AnswerInput(graphene.InputObjectType):
    id = graphene.ID()
    question = graphene.String()
    answer_text = graphene.String()
    is_right = graphene.Boolean()
    created_on = graphene.String()
    updated_on = graphene.String()

    def __str__(self):
        return self.title


class CreateAnswerMutation(graphene.Mutation):
    class Arguments:
        input = AnswerInput(required=True)
    answer = graphene.Field(AnswerType)

    @staticmethod
    def mutate(root, info, input):
        answer_instance = Answer(
            question=input.question,
            answer_text=input.answer_text,
            is_right=input.is_right,
        )
        answer_instance.save()
        return CreateAnswerMutation(answer=answer_instance)


class UpdateAnswerMutation(graphene.Mutation):
    class Arguments:
        input = AnswerInput(required=True)
    answer = graphene.Field(AnswerType)

    @staticmethod
    def mutate(root, info, input):
        answer_instance = Answer.object.get(id=input.id)
        if answer_instance:
            answer_instance.question = input.question
            answer_instance.answer_text = input.answer_text
            answer_instance.is_right = input.is_right
            answer_instance.save()
            return CreateAnswerMutation(answer=answer_instance)
        return UpdateAnswerMutation(answer=None)


class DeleteAnswerMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    answer = graphene.Field(AnswerType)

    @staticmethod
    def mutate(root, info, answer_id):
        answer_instance = Answer.objects.get(id=answer_id)
        if answer_instance:
            answer_instance.delete()
            return DeleteAnswerMutation(answer=None)
