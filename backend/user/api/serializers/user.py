from base.api.serializers import BaseDetailSerializer, BaseListCreateSerializer, BaseModelSerializer
from rest_framework import serializers

from community.api.serializers.event import EventsDetailSerializer, PostsDetailSerializer
from ...models import Profile
from django.contrib.auth.models import User

class ProfileDetailSerializer(BaseDetailSerializer):
    class Meta(BaseDetailSerializer.Meta):
        model = Profile
        fields = ['user_id', 'usename', 'email','date_of_birth', 'date_joined','designation', 'work_location']


#getting specific user's posts,events
class ProfilePostEventDetailSerializer(BaseDetailSerializer):
    post_details = serializers.SerializerMethodField('get_post_details')
    event_details = serializers.SerializerMethodField('get_event_details')

    class Meta(BaseDetailSerializer.Meta):
        model = User
        fields= ['id','username','email','post_details','event_details']
   

    def get_post_details(self, instance):
        return [PostsDetailSerializer(m).data for m in instance.createdby.filter(username=self.username)]
    
    def get_event_details(self, instance):
        return [EventsDetailSerializer(a).data for a in instance.event_postedby.filter(username=self.username)]
   
