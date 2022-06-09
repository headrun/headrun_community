from base.api.views import BaseListCreateView, BaseDetailView

from ..serializers.event import (
    EventsDetailSerializer,
    EventPhotosDetailSerializer
)


class EventsListCreateView(BaseListCreateView):
    serializer_class = EventsDetailSerializer


class EventPhotosDetailView(BaseDetailView):
    serializer_class = EventPhotosDetailSerializer
