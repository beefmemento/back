from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    
from rest_framework.views import APIView
from rest_framework.response import Response

class PostBySubjectView(APIView):
    def get(self, request, subject_title, format = None):
        print("subject_title:",subject_title)
        posts = Post.objects.filter(subject__title = subject_title)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
