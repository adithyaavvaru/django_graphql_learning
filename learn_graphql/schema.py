import apps.schema
import graphene


class Query(apps.schema.TopicsQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
