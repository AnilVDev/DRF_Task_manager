from django.urls import path

from .views import TaskCreateListView, TaskUpdateDeleteView

urlpatterns = [
    path("tasks/", TaskCreateListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskUpdateDeleteView.as_view(), name="task-detail"),
]
