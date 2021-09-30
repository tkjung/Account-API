from django.urls import path, include
from .views import RegistrationAPI, LoginAPI, UserAPI, ProfileList, ProfileDetail, UserList, UserDetail, ChangePasswordView
from knox import views as knox_views
urlpatterns = [
    path("auth/register/", RegistrationAPI.as_view()),
    path("auth/login/", LoginAPI.as_view()),
    path("auth/user/", UserAPI.as_view()),
    path("auth/list/", UserList.as_view()),
    path("auth/list/<int:pk>/", UserDetail.as_view()),
    path("auth/profile/", ProfileList.as_view()),
    path("auth/profile/<int:pk>/", ProfileDetail.as_view()),
    path('auth/logout/', knox_views.LogoutView.as_view()),
    path('auth/updatepw/', ChangePasswordView.as_view()),
]