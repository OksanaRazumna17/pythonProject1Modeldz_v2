from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import CategoryViewSet, TaskListCreateView, TaskDetailUpdateDeleteView, TaskStatsView, SubTaskListCreateView, SubTaskDetailUpdateDeleteView

# Создаем роутер для автоматической генерации маршрутов
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)  # Регистрируем CategoryViewSet

urlpatterns = [
    path('admin/', admin.site.urls),  # Маршрут для админки

    # Маршруты для задач (Tasks)
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailUpdateDeleteView.as_view(), name='task-detail-update-delete'),
    path('tasks/stats/', TaskStatsView.as_view(), name='task-stats'),

    # Маршруты для подзадач (SubTasks)
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),

    # Включаем маршруты для категорий
    path('', include(router.urls)),  # Подключаем автоматически сгенерированные маршруты
]

