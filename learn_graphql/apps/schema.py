from graphene_django import DjangoObjectType
import graphene

from .topics.models import Topic as TopicModel


class Topic(DjangoObjectType):
    class Meta:
        model = TopicModel


class Query(graphene.ObjectType):
    topics = graphene.List(Topic)

    def resolve_topics(self, info):
        return TopicModel.objects.all()


schema = graphene.Schema(query=Query)
