from collections import defaultdict
from promise import Promise
from promise.dataloader import DataLoader
from blog.models import Comment


class CommentsByArticleIdLoader(DataLoader):
    def batch_load_fn(self, article_ids):
        comments_by_article_ids = defaultdict(list)

        for comment in Comment.objects.filter(article_id__in=article_ids).iterator():
            comments_by_article_ids[comment.article_id].append(comment)

        return Promise.resolve([comments_by_article_ids.get(article_id, [])
                                for article_id in article_ids])
