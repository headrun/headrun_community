from base.api.views import BaseListCreateUpdateView, BaseDetailView, BaseListCreateView

from ..serializers.event import (
    CommentsDetailSerializer,
    EventsDetailSerializer,
    EventPhotosDetailSerializer,
    FeadbackDetailSerializer,
    PostsDetailSerializer,
    FileTypeDetailSerializer,
    ReactionsDetailSerializer
)


class EventsListCreateView(BaseListCreateUpdateView):
    serializer_class = EventsDetailSerializer


class EventPhotosDetailView(BaseDetailView):
    serializer_class = EventPhotosDetailSerializer


class FeedbackListCreateView(BaseListCreateUpdateView):
    serializer_class = FeadbackDetailSerializer


class PostsListCreateView(BaseListCreateUpdateView):
    serializer_class = PostsDetailSerializer
    

class FileTypeDetailView(BaseListCreateUpdateView):
    serializer_class = FileTypeDetailSerializer
    

class CommentsListCreateView(BaseListCreateUpdateView):
    serializer_class = CommentsDetailSerializer
    
    
class ReactionsDetailView(BaseListCreateUpdateView):
    serializer_class = ReactionsDetailSerializer