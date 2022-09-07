from django.test import TestCase
from django.contrib.auth.hashers import (
    make_password
)

from rest_framework import exceptions

from post.models import Post as PostModel
from post.service.post_service import (
    post_create_service,
    post_check_password,
)



class PostServiceView(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        TestCase를 위한 TestDB에 데이터 저장
        """
        post_1 = PostModel.objects.create(
            title="title",
            content="content",
            password=make_password("password1")
        )

    # 게시글 작성 테스트
    
    def test_post_create(self):
        """
            게시글 작성 테스트

            Case : 정상 작동
        """

        post_info = {
            "title": "title",
            "content": "content",
            "password": "password1"
        }

        pre_count = PostModel.objects.all().count()
        
        with self.assertNumQueries(1):
            new_post = post_create_service(post_info)
        
        cur_count = PostModel.objects.all().count()

        self.assertEqual(pre_count + 1, cur_count)


    def test_post_create_when_password_is_less_then_six(self):
        """
            게시글 작성 테스트

            Case : 비밀번호가 6글자보다 짧을 경우
        """

        post_info = {
            "title": "title",
            "content": "content",
            "password": "pass1"
        }

        with self.assertRaisesMessage(
           exceptions.ValidationError,
           "{'detail': [ErrorDetail(string='비밀번호는 6글자 이상이어야합니다', code='invalid')]}" 
        ):
            new_post = post_create_service(post_info)


    def test_post_create_when_number_does_not_exist_in_password(self):
        """
            게시글 작성 테스트

            Case : 비밀번호에 숫자가 포함되지 않은 경우
        """

        post_info = {
            "title": "title",
            "content": "content",
            "password": "password"
        }

        with self.assertRaisesMessage(
           exceptions.ValidationError,
            "{'detail': [ErrorDetail(string='비밀번호는 숫자를 1개이상 포함해야합니다.', code='invalid')]}" 
        ):
            new_post = post_create_service(post_info)

    
    def test_post_create_when_title_is_out_of_range(self):
        """
            게시글 작성 테스트

            Case : 제목이 범위를 벗어난 경우
        """

        post_info = {
            "title": "title" * 5,
            "content": "content",
            "password": "password1"
        }

        with self.assertRaisesMessage(
           exceptions.ValidationError,
            "{'title': [ErrorDetail(string='Ensure this field has no more than 20 characters.', code='max_length')]}"
        ):
            new_post = post_create_service(post_info)


    def test_post_create_when_title_is_blank(self):
        """
            게시글 작성 테스트

            Case : 제목이 빈칸인 경우
        """

        post_info = {
            "title": "",
            "content": "content",
            "password": "password1"
        }

        with self.assertRaisesMessage(
           exceptions.ValidationError,
            "{'title': [ErrorDetail(string='This field may not be blank.', code='blank')]}"
        ):
            new_post = post_create_service(post_info)


    def test_post_create_when_content_is_blank(self):
        """
            게시글 작성 테스트

            Case : 내용이 빈칸인 경우
        """

        post_info = {
            "title": "title",
            "content": "",
            "password": "password1"
        }

        with self.assertRaisesMessage(
           exceptions.ValidationError,
           "{'content': [ErrorDetail(string='This field may not be blank.', code='blank')]}"
        ):
            new_post = post_create_service(post_info)


    def test_post_create_when_content_is_out_of_range(self):
        """
            게시글 작성 테스트

            Case : 내용이 범위를 벗어난 경우
        """

        post_info = {
            "title": "title",
            "content": "content" * 30,
            "password": "password1"
        }

        with self.assertRaisesMessage(
           exceptions.ValidationError,
           "{'content': [ErrorDetail(string='Ensure this field has no more than 200 characters.', code='max_length')]}"
        ):
            new_post = post_create_service(post_info)


    # 게시글 비밀번호 확인 테스트

    def test_post_check_password(self):
        """ 
            게시글 비밀번호 확인 테스트

            Case : 옳바른 비밀번호 입력한 경우
        """
    
        post_obj = PostModel.objects.filter(title="title").first()
        
        raw_password = "password1"

        self.assertEqual(post_check_password(raw_password, post_obj), True)


    def test_post_check_password_when_raw_password_is_incorrect(self):
        """ 
            게시글 비밀번호 확인 테스트

            Case : 옳바르지 않은 비밀번호 입력한 경우
        """
        
        post_obj = PostModel.objects.filter(title="title").first()
        
        raw_password = "password2"

        self.assertEqual(post_check_password(raw_password, post_obj), False)

