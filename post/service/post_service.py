from post.models import Post as PostModel
from post.serializers import PostModelSerializer


def post_get_service(page):

    post_obj_all = PostModel.objects.all()


    return PostModelSerializer(post_obj_all, many=True).data