from .views.event import CommentsListCreateView, EventReactionsDetailView, EventsListCreateView, EventPhotosDetailView, FeedbackListCreateView, FileTypeDetailView, PostsListCreateView, ReactionsDetailView

version = 1

views = [
    EventsListCreateView,
    EventPhotosDetailView,
    FeedbackListCreateView,
    EventReactionsDetailView,
    PostsListCreateView,
    FileTypeDetailView,
    CommentsListCreateView,
    ReactionsDetailView
]

urlpatterns = []
[urlpatterns.extend(view.urlpatterns(version)) for view in views]
