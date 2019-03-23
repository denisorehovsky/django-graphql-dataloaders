from django.utils.functional import cached_property
from gql.loaders import CommentsByArticleIdLoader


class GQLContext:

    def __init__(self, request):
        self.request = request

    @cached_property
    def user(self):
        return self.request.user

    @cached_property
    def comments_by_article_id_loader(self):
        return CommentsByArticleIdLoader()
