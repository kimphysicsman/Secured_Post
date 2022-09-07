from rest_framework import serializers

from post.models import Post as PostModel


class PostModelSerializer(serializers.ModelSerializer):
    
    # def create(self, *args, **kwargs):
    #     user = super().create(*args, **kwargs)
    #     p = user.password
    #     user.set_password(p)
    #     user.save()
    #     return user

    # def update(self, instance, validated_data):
    #     for key, value in validated_data.items():
    #         if key == "password":
    #             instance.set_password(value)
    #             continue
    #         setattr(instance, key, value)
    #     instance.save()

    #     return instance


    class Meta:
        model = PostModel
        fields = ["id", "title", "content", "password", "created_at", "updated_at"
        ]

        extra_kwargs = {
            'password': {'write_only': True}
        }
