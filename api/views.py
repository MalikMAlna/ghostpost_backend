from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import PostSerializer
from ghostpost.models import Post


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    basename = 'post'
    queryset = Post.objects.all()

    # @action(detail=False)
    # def highest_rated(self, request):
    #     highest_rated = Post.objects.all().order_by('total_vote')
    #     serializer = self.get_serializer(highest_rated, many=True)
    #     return Response(serializer.data)

    @action(detail=False)
    def boast(self, request):
        boast = Post.objects.filter(b_or_r=True)
        serializer = self.get_serializer(boast, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roast(self, request):
        roast = Post.objects.filter(b_or_r=False)
        serializer = self.get_serializer(roast, many=True)
        return Response(serializer.data)
