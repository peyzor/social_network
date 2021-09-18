from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Post, PostLike
from .serializer_fields import PostLikeHyperlinkedRelatedField
from profiles.serializer_fields import UserHyperlinkedRelatedField


class PostSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='posts:post_detail',
        lookup_url_kwarg='post_id',
    )
    parent = serializers.HyperlinkedRelatedField(view_name='posts:post_detail',
                                                 lookup_url_kwarg='post_id',
                                                 read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)
    user = UserHyperlinkedRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'url', 'parent', 'user', 'likes_count', 'content', 'image',
            'created_time'
        ]

    def get_likes_count(self, obj):
        return obj.likes.count()


class PostLikeSerializer(serializers.ModelSerializer):
    url = PostLikeHyperlinkedRelatedField(source='*', read_only=True)
    user = UserHyperlinkedRelatedField(read_only=True)
    post = serializers.HyperlinkedRelatedField(view_name='posts:post_detail',
                                               lookup_url_kwarg='post_id',
                                               read_only=True)

    class Meta:
        model = PostLike
        fields = ['url', 'user', 'post', 'created_time']