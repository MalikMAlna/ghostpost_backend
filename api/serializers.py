from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ghostpost.models import Post


class PostSerializer(ModelSerializer):
    total_vote = serializers.SerializerMethodField()

    def get_total_vote(self, obj):
        return obj.up_vote - obj.down_vote

    class Meta:
        model = Post
        fields = ('id', 'b_or_r', 'content', 'up_vote', 'down_vote', 'created', 'total_vote')
