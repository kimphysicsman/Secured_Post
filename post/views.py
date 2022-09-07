from mmap import PAGESIZE
from rest_framework.views import APIView
from rest_framework import status, exceptions
from rest_framework.response import Response


from post.models import Post as PostModel
from post.serializers import (
    PostModelSerializer,
)
from post.service.post_service import (
    post_get_service,
    post_create_service,
    post_update_service,
    post_delete_service,
    post_check_password,
)

# 게시글 CRUD View
class PostView(APIView):

    # 게시글 조회
    def get(self, request):
        # 조회할 페이지, default = 1
        page = request.GET.get('page', "1")

        # page index 값을 page -1 값으로 전달
        post_list_of_page = post_get_service(int(page)-1)

        return Response(post_list_of_page, status=status.HTTP_200_OK)

    # 게시글 작성
    def post(self, request):
        try:
            new_post = post_create_service(request.data)
            return Response(new_post, status=status.HTTP_200_OK) 
        
        except exceptions.ValidationError as e:
            error_key = list(e.detail.keys())[0]
            error_detail = e.detail.get(error_key, "")

            if error_key == "title":
                if error_detail[0].code == "blank":
                    return Response({"error": "제목이 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                elif error_detail[0].code == "max_length":
                    return Response({"error": "제목을 20글자 이하로 작성해주세요."}, status=status.HTTP_400_BAD_REQUEST) 
            
            elif error_key == "content":
                if error_detail[0].code == "blank":
                    return Response({"error": "내용이 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                elif error_detail[0].code == "max_length":
                    return Response({"error": "내용을 200글자 이하로 작성해주세요."}, status=status.HTTP_400_BAD_REQUEST) 

            elif error_key == "detail":
                return Response({"error": error_detail[0]}, status=status.HTTP_400_BAD_REQUEST) 
                
            return Response({"error": "게시글 작성에 실패했습니다."}, status=status.HTTP_400_BAD_REQUEST) 

    # 게시글 수정
    def put(self, request, post_id):
        try:
            post_obj = PostModel.objects.get(id=post_id)
        except:
            return Response({"error": "해당 게시글을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        
        password = request.data.pop('password', "")
        if not post_check_password(password, post_obj):
            return Response({"error": "비밀번호가 옳바르지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            update_info = post_update_service(post_obj, request.data)
            return Response(update_info, status=status.HTTP_200_OK)
        
        except exceptions.ValidationError as e:
            error_key = list(e.detail.keys())[0]
            error_detail = e.detail.get(error_key, "")
            
            if error_key == "title":
                if error_detail[0].code == "blank":
                    return Response({"error": "제목이 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                elif error_detail[0].code == "max_length":
                    return Response({"error": "제목을 20글자 이하로 작성해주세요."}, status=status.HTTP_400_BAD_REQUEST) 
            
            elif error_key == "content":
                if error_detail[0].code == "blank":
                    return Response({"error": "내용이 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                elif error_detail[0].code == "max_length":
                    return Response({"error": "내용을 200글자 이하로 작성해주세요."}, status=status.HTTP_400_BAD_REQUEST) 

        return Response({"error" : "게시글 수정에 실패했습니다."}, status=status.HTTP_400_BAD_REQUEST)

     # 게시글 수정
    def delete(self, request, post_id):
        try:
            post_obj = PostModel.objects.get(id=post_id)
        except:
            return Response({"error": "해당 게시글을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        
        password = request.data.pop('password', "")
        if not post_check_password(password, post_obj):
            return Response({"error": "비밀번호가 옳바르지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)

        post_delete_service(post_obj)
        return Response({"detail": "게시글이 삭제 되었습니다."}, status=status.HTTP_200_OK)
        
