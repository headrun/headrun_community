from base.api.views import BaseListCreateUpdateView, BaseDetailView, BaseListCreateView
from api.serializers import user



class ProfileListCreateView(BaseListCreateUpdateView):
    serializer_class = user.ProfileDetailSerializer

