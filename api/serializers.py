from rest_framework.serializers import ModelSerializer

from ghostpost.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'b_or_r', 'content', 'up_vote', 'down_vote', 'created', 'total_vote')


