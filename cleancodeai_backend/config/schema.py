#Project Level Schema Inheritance for GraphQL

from graphene import ObjectType, Schema
from apps.authentication import schema as AuthenticationSchema

class Query(
    AuthenticationSchema.Query,
    ObjectType
):
    pass

class Mutation(
    AuthenticationSchema.Mutation,
    ObjectType
):
    pass

schema = Schema(query=Query, mutation=Mutation)
