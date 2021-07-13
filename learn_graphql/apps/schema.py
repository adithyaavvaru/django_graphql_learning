from graphene_django import DjangoObjectType
import graphene

from .topics.models import Topic as TopicModel
from graphql.error import GraphQLLocatedError


class Topic(DjangoObjectType):
    class Meta:
        model = TopicModel


class TopicsQuery(graphene.ObjectType):
    get_topics = graphene.List(Topic)
    get_topic_by_name = graphene.Field(Topic, name=graphene.String(required=True))

    def resolve_get_topics(self, info):
        return TopicModel.objects.all()

    def resolve_get_topic_by_name(self, info, name):
        val = TopicModel.objects.filter(topic_name=name).first()
        if not val:
            raise AttributeError("There is no topic by name : '" + name + "'")
        print(val)
        return val

