#Project Level Schema Inheritance for GraphQL

from graphene import ObjectType, Schema
import web_backend.system_app.schema as system_app_schema

class Query(
    system_app_schema.Query,
    ObjectType
):
    pass

class Mutation(
    system_app_schema.Mutation,
    ObjectType
):
    pass

schema = Schema(query=Query, mutation=Mutation)
