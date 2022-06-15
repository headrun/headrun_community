from base.api.views import BaseListCreateUpdateView, BaseListView
from ..serializers.user import ProfileListCreateSerializer, ProfilePostEventDetailSerializer


class ProfileListCreateView(BaseListCreateUpdateView):
    serializer_class = ProfileListCreateSerializer


class ProfilePostListView(BaseListView):
    serializer_class = ProfilePostEventDetailSerializer
