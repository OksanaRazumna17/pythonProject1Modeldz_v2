from django.contrib import admin
from django.urls import path
from tasks.views import TaskCreateView, TaskListView, SubTaskListCreateView, SubTaskDetailUpdateDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),
    path('', TaskListView.as_view(), name='home'),
]
