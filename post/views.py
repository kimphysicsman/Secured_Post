from mmap import PAGESIZE
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from post.service.post_service import (
    post_get_service,
)

# 게시글 CRUD View
class PostView(APIView):
    # 게시글 조회
    def get(self, request):
        page = request.GET.get('page', "")

        post_all = post_get_service(page)

        return Response(post_all, status=status.HTTP_200_OK)