from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api import views

# urlpatterns
urlpatterns = [
    path("todo/", views.TasksView.as_view(), name="task_list"),
    path("categories/", views.CategoryView.as_view(), name="category_list"),
    path("categories/<int:pk>/", views.CategoryDetail.as_view(), name="category_detail"),
    path("users/", views.UserList.as_view(), name="user_list"),
    path("users/<int:pk>", views.UserDetail.as_view(), name="user_detail"),
    path("register/", views.UserCreation.as_view(), name="user_registration"),
    path("logout/", views.SignOut.as_view(), name="logout"),

    # simplejwt
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]