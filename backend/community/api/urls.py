from .views.event import (
    AllPostsDetailView,
    CommentsListCreateView,
    EventReactionsDetailView,
    EventsListCreateView,
    EventPhotosDetailView,
    FeedbackListCreateView,
    FileTypeDetailView,
    PostsListCreateView,
    ReactionsDetailView)

version = 1

views = [
    EventsListCreateView,
    EventPhotosDetailView,
    FeedbackListCreateView,
    EventReactionsDetailView,
    PostsListCreateView,
    AllPostsDetailView,
    FileTypeDetailView,
    CommentsListCreateView,
    ReactionsDetailView
]

urlpatterns = []
[urlpatterns.extend(view.urlpatterns(version)) for view in views]
