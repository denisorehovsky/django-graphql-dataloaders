from graphene_django.views import GraphQLView
from gql.context import GQLContext


class CustomGraphQLView(GraphQLView):

    def get_context(self, request):
        return GQLContext(request)
