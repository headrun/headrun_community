from django.shortcuts import render
from api.serializers import ProfileSerializer
from userapp.model.models import Profile
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)