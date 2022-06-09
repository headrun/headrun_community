from django.contrib import admin
from django.urls import path,include
from user.api.views.views import RegisterView, LoginView, UserView, LogoutView
from user.api.views import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register',RegisterView.as_view()),
    path('api/login', LoginView.as_view()),
    path('api/user', UserView.as_view()),
    path('api/logout', LogoutView.as_view()),
]