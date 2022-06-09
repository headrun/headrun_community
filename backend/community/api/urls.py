from .views.event import EventsListCreateView, EventPhotosDetailView

version = 1

views = [
    EventsListCreateView,
    EventPhotosDetailView

]

urlpatterns = []
[urlpatterns.extend(view.urlpatterns(version)) for view in views]
