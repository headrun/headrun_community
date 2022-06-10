from user.api.views.userviews import ProfileListCreateView

version = 1

views = [
    ProfileListCreateView
    
]

urlpatterns = []
[urlpatterns.extend(view.urlpatterns(version)) for view in views]
