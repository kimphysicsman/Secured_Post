from django.contrib.auth.hashers import make_password

from rest_framework import serializers

from post.models import Post as PostModel


# Post 모델 생성을 위한 Serializer
class PostModelCreateSerializer(serializers.ModelSerializer):
    
    def validate(self, data):
        # 비밀번호 : 6글자 이상, 숫자 1개 이상 포함
        password = data.get("password", "")
        if len(password) < 6:
            raise serializers.ValidationError(
                    detail={"detail": "비밀번호는 6글자 이상이어야합니다"},
                )

        number_check = any([char in "0123456789" for char in password])
        if not number_check:
            raise serializers.ValidationError(
                    detail={"detail": "비밀번호는 숫자를 1개이상 포함해야합니다."},
                )        
        
        return data

    # 게시글 생성 시 password 해시
    def create(self, validated_data):
        password = validated_data.pop("password", "")
        validated_data["password"] = make_password(password)

        new_post = PostModel.objects.create(**validated_data)
         
        return new_post


    class Meta:
        model = PostModel
        fields = ["id", "title", "content", "password", "created_at", "updated_at"
        ]

        extra_kwargs = {
            'password': {'write_only': True}
        }


# 게시글 조회, 수정, 삭제를 위한 Serializer
class PostModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostModel
        fields = ["id", "title", "content", "password", "created_at", "updated_at"
        ]

        extra_kwargs = {
            'password': {'write_only': True}
        }
