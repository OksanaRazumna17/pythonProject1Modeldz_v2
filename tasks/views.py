from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Count
from .models import Task, SubTask
from .serializers import TaskSerializer, TaskDetailSerializer, TaskCreateSerializer, SubTaskSerializer, SubTaskCreateSerializer

# Представление для создания задачи с использованием TaskCreateSerializer
class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer  # Используем сериализатор с валидацией дедлайна

# Представление для получения списка задач с фильтрацией и пагинацией
class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # Фильтрация по статусу и дедлайну
    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get('status')
        deadline = self.request.query_params.get('deadline')
        if status:
            queryset = queryset.filter(status=status)
        if deadline:
            queryset = queryset.filter(deadline__lte=deadline)
        return queryset

# Агрегирующее представление для получения статистики задач
class TaskStatsView(APIView):
    def get(self, request, *args, **kwargs):
        total_tasks = Task.objects.count()
        tasks_by_status = Task.objects.values('status').annotate(count=Count('status'))
        overdue_tasks = Task.objects.filter(deadline__lt=timezone.now()).count()

        stats = {
            'total_tasks': total_tasks,
            'tasks_by_status': tasks_by_status,
            'overdue_tasks': overdue_tasks,
        }
        return Response(stats)

# Представление для создания и получения списка подзадач
class SubTaskListCreateView(generics.ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer  # Используем сериализатор для создания подзадач

# Представление для получения, обновления и удаления подзадач
class SubTaskDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer

