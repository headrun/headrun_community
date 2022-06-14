from base.api.views import BaseListCreateUpdateView, BaseDetailView

from ..serializers.event import (
    AllPostDetailSerializer,
    CommentsDetailSerializer,
    EventsDetailSerializer,
    EventPhotosDetailSerializer,
    FeadbackDetailSerializer,
    EventReactionsDetailSerializer,
    PostsDetailSerializer,
    FileTypeDetailSerializer,
    ReactionsDetailSerializer
)


class EventsListCreateView(BaseListCreateUpdateView):
    serializer_class = EventsDetailSerializer


class EventPhotosDetailView(BaseListCreateUpdateView):
    serializer_class = EventPhotosDetailSerializer


class FeedbackListCreateView(BaseListCreateUpdateView):
    serializer_class = FeadbackDetailSerializer
    
    
class EventReactionsDetailView(BaseListCreateUpdateView):
    serializer_class = EventReactionsDetailSerializer


class PostsListCreateView(BaseListCreateUpdateView):
    serializer_class = PostsDetailSerializer
    

class FileTypeDetailView(BaseListCreateUpdateView):
    serializer_class = FileTypeDetailSerializer
    

class CommentsListCreateView(BaseListCreateUpdateView):
    serializer_class = CommentsDetailSerializer
    
    
class ReactionsDetailView(BaseListCreateUpdateView):
    serializer_class = ReactionsDetailSerializer
    
    
class AllPostsDetailView(BaseListCreateUpdateView):
    serializer_class = AllPostDetailSerializer
