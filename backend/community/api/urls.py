from .views.event import CommentsListCreateView, EventsListCreateView, EventPhotosDetailView, FeedbackListCreateView, FileTypeDetailView, PostsListCreateView, ReactionsDetailView

version = 1

views = [
    EventsListCreateView,
    EventPhotosDetailView,
    FeedbackListCreateView,
    PostsListCreateView,
    FileTypeDetailView,
    CommentsListCreateView,
    ReactionsDetailView
]

urlpatterns = []
[urlpatterns.extend(view.urlpatterns(version)) for view in views]
