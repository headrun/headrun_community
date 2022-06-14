from base.api.views import BaseListCreateUpdateView
from api.serializers import user



class ProfileListCreateView(BaseListCreateUpdateView):
    serializer_class = user.ProfileDetailSerializer


class ProfilePostListCreateView(BaseListCreateUpdateView):
    serializer_class= user.ProfilePostEventDetailSerializer
