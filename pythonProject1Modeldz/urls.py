from django.contrib import admin
from django.urls import path
from tasks.views import TaskListCreateView, TaskDetailUpdateDeleteView, TaskStatsView
from tasks.views import SubTaskListCreateView, SubTaskDetailUpdateDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Маршруты для задач (Tasks)
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailUpdateDeleteView.as_view(), name='task-detail-update-delete'),
    path('tasks/stats/', TaskStatsView.as_view(), name='task-stats'),

    # Маршруты для подзадач (SubTasks)
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),
]



