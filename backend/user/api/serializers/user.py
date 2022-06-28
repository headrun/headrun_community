from django.contrib.auth.models import User
from rest_framework import serializers

from base.api.serializers import BaseDetailSerializer, BaseListCreateSerializer
from community.api.serializers.event import EventsDetailSerializer, PostsDetailSerializer
from ...models import Profile


class UserDetailSerializer(BaseDetailSerializer):
    class Meta(BaseDetailSerializer.Meta):
        model = User
        fields = ['id', 'username', 'email']


class ProfileListCreateSerializer(BaseListCreateSerializer):
    user = serializers.SerializerMethodField()

    class Meta(BaseListCreateSerializer.Meta):
        model = Profile
        fields = ['user', 'date_of_birth', 'designation', 'work_location']

    def get_user(self, instance):
        return UserDetailSerializer(instance.user).data


# getting specific user's posts,events
class ProfilePostEventDetailSerializer(BaseDetailSerializer):
    post_details = serializers.SerializerMethodField('get_post_details')
    event_details = serializers.SerializerMethodField('get_event_details')

    class Meta(BaseDetailSerializer.Meta):
        model = User
        fields = ['id', 'username', 'email', 'post_details', 'event_details']

    def get_post_details(self, instance):
        import pdb;pdb.set_trace()
        return [PostsDetailSerializer(m).data for m in instance.createdby.all()]

    def get_event_details(self, instance):
        return [EventsDetailSerializer(a).data for a in instance.createdby.all()]
