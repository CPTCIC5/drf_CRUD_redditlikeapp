from django.shortcuts import render
from rest_framework import generics,permissions
from .serializiers import PostSerializer
from .models import Post,Vote
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.views.decorators.cache import cache_page
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from rest_framework.decorators import throttle_classes

class IndexView(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    cache_page=(60*(60*2))
    throttle_classes=[AnonRateThrottle,UserRateThrottle]

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)

'''
@api_view(['GET','POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def indexview(request):
    q=Post.objects.all()
    s1=PostSerializer(q,many=True)
    return Response(s1.data)'''

@api_view(['GET','DELETE'])
@cache_page(60*60*2)
@throttle_classes([UserRateThrottle])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def detailview(request,post_id):
    if request.method=='GET':
        tasks=Post.objects.get(id=post_id)
        serializer= PostSerializer(tasks, many=False)
        return Response(serializer.data)
        
    if request.method=='DELETE':
        post=Post.objects.get(id=post_id)
        if post.author == request.user:
            post.delete()
            return Response("Sucess,Deleted!!")
        else:
            return Response("U cannot delete any other user posts BRUH!!")