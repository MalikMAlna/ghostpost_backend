from rest_framework.viewsets import ModelViewSet

from api.serializers import PostSerializer
from ghostpost.models import Post


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    basename = 'post'
    queryset = Post.objects.all()