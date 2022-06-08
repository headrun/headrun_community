import datetime

from django.shortcuts import render
from api.serializers import PostSerializer,EventSerializer
# from community.model.Eventmodels import Events
from community.model.poststorymodels import Posts
from community.model.Eventsmodels import Events
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
# Create your views here.
    
class GetPosts(generics.ListCreateAPIView):
    queryset = Posts.objects.filter(post_type='POST')
    print(queryset, "POST TYPE")
    serializer_class = PostSerializer
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    
# class UpdatePost(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Posts.objects.get(id=1)
#     serializer_class = PostSerializer
#     lookup_field="id"
#     def get_queryset(self):
#         return Posts.objects.filter(owner=self.request.user)

@api_view(['PUT'])
def updatepost(request, id):
    postobj=Posts.objects.get(id=id)
    serializer= PostSerializer(instance = postobj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def delete_post(request,id):
    postobj=Posts.objects.get(id=id)
    postobj.delete()
    return Response("one post is deleted")

class GetStory(generics.ListCreateAPIView):
    YstdDateTime = datetime.datetime.now()-datetime.timedelta(hours=24)
    print('24 hours ago',YstdDateTime)
    #queryset = Posts.objects.filter(created_at <= YstdDateTime)
    # created_at = Posts.created_at
    # print(created_at,"****************************")
    queryset = Posts.objects.filter(post_type='STORY', created_at__gt=YstdDateTime)
    serializer_class = PostSerializer
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['PUT'])
def updatestory(request, id):
    storyobj=Posts.objects.get(id=id)
    print(storyobj)
    serializer= PostSerializer(instance = storyobj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def delete_story(request,id):
    storyobj=Posts.objects.get(id=id)
    storyobj.delete()
    return Response("one story is deleted")

class EventDetails(generics.ListCreateAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

@api_view(['PUT'])
def updateEvent(request, id):
    eventobj=Events.objects.get(id=id)
    print(eventobj)
    serializer= EventSerializer(instance = eventobj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def deleteEvent(request,id):
    eventobj=Events.objects.get(id=id)
    eventobj.delete()
    return Response("one Event is deleted")