from django.db import models

class Post(models.Model):
    """
        게시글 모델 
    """

    title = models.CharField("제목", max_length=20)
    content = models.CharField("내용", max_length=200)
    password = models.CharField("비밀번호", max_length=200)
    created_at = models.DateTimeField("생성시간", auto_now_add=True)
    updated_at = models.DateTimeField("수정시간", auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.title}"