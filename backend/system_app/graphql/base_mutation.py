import graphene

#To default the code and message variable
class BaseMutation(graphene.Mutation):
    code = graphene.String()
    message = graphene.String()

    def mutate(root, info):
        pass