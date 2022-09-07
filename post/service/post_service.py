from django.contrib.auth.hashers import (
    check_password,
)

from post.models import Post as PostModel
from post.serializers import (
    PostModelCreateSerializer,
    PostModelSerializer,
)



def post_get_service(page: int):
    """게시글 조회 서비스

    Args:
        page (int): 20개 단위의 페이지별 게시글 중 반환할 페이지

    Returns:
        (list): 해당 페이지의 게시글 정보가 담긴 리스트
    """


    post_obj_all = PostModel.objects.all().order_by("created_at")

    start_idx = page * 20
    end_idx = start_idx + 20

    if len(post_obj_all) < start_idx or page < 0:
        return []
    else:
        return PostModelSerializer(post_obj_all[start_idx:end_idx], many=True).data


def post_create_service(post_info: dict):
    """게시글 작성 서비스

    Args:
        post_info (dict): 생성할 게시글 정보

    Returns:
        (dict) : 생성한 게시글 정보
    """

    post_serializer = PostModelCreateSerializer(data=post_info)

    post_serializer.is_valid(raise_exception=True)
    post_serializer.save()

    return post_serializer.data


def post_update_service(post_obj: PostModel, update_info: dict):
    """게시글 수정 서비스

    Args:
        post_obj (PostModel): 수정할 게시글 오브젝트
        update_info (dict): 수정할 게시글 정보

    Returns:
        (dict) : 수정한 게시글 정보
    """
    post_serializer = PostModelSerializer(post_obj, data=update_info, partial=True)

    post_serializer.is_valid(raise_exception=True)
    post_serializer.save()

    return post_serializer.data


def post_delete_service(post_obj: PostModel):
    """게시글 삭제 서비스

    Args:
        post_obj (PostModel): 삭제할 게시글 오브젝트

    """
    
    post_obj.delete()
     


def post_check_password(raw_password: str, post_obj: PostModel) -> bool:
    """입력한 비밀번호와 게시글 비밀번호 일치 여부 확인 기능 

    Args:
        raw_password (str): 입력한 비밀번호
        post_obj (PostModel): 해당 게시글 오브젝트

    Returns:
        (bool) : 일치 여부
    """

    return bool(check_password(raw_password, post_obj.password))



