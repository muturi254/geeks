from django.urls import path

from api import views

# urlpatterns
urlpatterns = [
    path("", views.TasksView.as_view(), name="task_list"),
    path("categories/", views.CategoryView.as_view(), name="category_list"),
    path("categories/<int:pk>/", views.CategoryDetail.as_view(), name="category_detail"),
    path("users/", views.UserList.as_view(), name="user_list"),
    path("users/<int:pk>", views.UserDetail.as_view(), name="user_detail"),
]