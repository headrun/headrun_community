from base.api.views import BaseListCreateUpdateView, BaseDetailView

from ..serializers.event import (
    EventsDetailSerializer,
    EventPhotosDetailSerializer
)


class EventsListCreateView(BaseListCreateUpdateView):
    serializer_class = EventsDetailSerializer


class EventPhotosDetailView(BaseDetailView):
    serializer_class = EventPhotosDetailSerializer
