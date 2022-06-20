from base.api.views import BaseListCreateUpdateView, BaseListCreateView

from ..serializers.event import (
    
    CommentsDetailSerializer,
    EventsDetailSerializer,
    EventPhotosDetailSerializer,
    FeadbackDetailSerializer,
    EventReactionsDetailSerializer,
    PostTypeDetailSerializer,
    PostTypeDetailSerializer,
    PostsDetailSerializer,
    FileTypeDetailSerializer,
    ReactionsDetailSerializer,
    StoriesDetailSerializer
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
    
    
class PostTypeListCreateView(BaseListCreateUpdateView):
    serializer_class = PostTypeDetailSerializer
    

class FileTypeDetailView(BaseListCreateUpdateView):
    serializer_class = FileTypeDetailSerializer
    

class CommentsListCreateView(BaseListCreateUpdateView):
    serializer_class = CommentsDetailSerializer
    
    
class ReactionsDetailView(BaseListCreateUpdateView):
    serializer_class = ReactionsDetailSerializer


class StoriesDetailView(BaseListCreateView):
    view_name = 'stories'
    url_path = '/' + view_name + '/$'
    serializer_class = StoriesDetailSerializer
