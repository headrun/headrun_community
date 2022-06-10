from .views.event import EventsListCreateView, EventPhotosDetailView, FeedbackListCreateView

version = 1

views = [
    EventsListCreateView,
    EventPhotosDetailView,
    FeedbackListCreateView

]

urlpatterns = []
[urlpatterns.extend(view.urlpatterns(version)) for view in views]
