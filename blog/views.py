from rest_framework.generics import ListCreateAPIView
from .serializers import PostSerializer
from .models import Post


class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer