from .views.userviews import ProfileListCreateView, ProfilePostListCreateView

version = 1

views = [
    ProfileListCreateView,
    ProfilePostListCreateView
    
]

urlpatterns = []
[urlpatterns.extend(view.urlpatterns(version)) for view in views]
