from .views.event import (
    CommentsListCreateView,
    EventReactionsDetailView,
    EventsListCreateView,
    EventPhotosDetailView,
    FeedbackListCreateView,
    FileTypeDetailView,
    PostsListCreateView,
    ReactionsDetailView,
    StoriesDetailView)

version = 1

views = [
    EventsListCreateView,
    EventPhotosDetailView,
    FeedbackListCreateView,
    EventReactionsDetailView,
    PostsListCreateView,
    FileTypeDetailView,
    CommentsListCreateView,
    ReactionsDetailView,
    StoriesDetailView
]

urlpatterns = []
[urlpatterns.extend(view.urlpatterns(version)) for view in views]
