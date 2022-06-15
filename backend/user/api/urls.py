from .views.userviews import ProfileListCreateView, ProfilePostListView

version = 1

views = [
    ProfileListCreateView,
    ProfilePostListView
    
]

urlpatterns = []
[urlpatterns.extend(view.urlpatterns(version)) for view in views]
