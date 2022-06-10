from base.api.serializers import BaseDetailSerializer, BaseListCreateSerializer, BaseModelSerializer

from ...models import Profile


class ProfileDetailSerializer(BaseDetailSerializer):
    class Meta(BaseDetailSerializer.Meta):
        model = Profile
        fields = ['user_id', 'usename', 'email','date_of_birth', 'date_joined','designation', 'work_location']
