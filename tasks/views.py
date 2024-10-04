from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from django.db.models import Count
from .models import Task, SubTask, Category
from .serializers import TaskSerializer, TaskCreateSerializer, TaskDetailSerializer, SubTaskSerializer, SubTaskCreateSerializer, CategorySerializer


# Представление для создания и получения списка задач с пагинацией, фильтрацией, поиском и сортировкой
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Фильтрация по статусу и дедлайну
        status = self.request.query_params.get('status')
        deadline = self.request.query_params.get('deadline')
        if status:
            queryset = queryset.filter(status=status)
        if deadline:
            queryset = queryset.filter(deadline__lte=deadline)

        # Поиск по title и description
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(title__icontains=search) | queryset.filter(description__icontains=search)

        # Сортировка по created_at
        queryset = queryset.order_by('created_at')

        return queryset


# Представление для получения, обновления и удаления задачи
class TaskDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer


# Агрегирующее представление для получения статистики задач
class TaskStatsView(generics.GenericAPIView):
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


# Представление для создания и получения списка подзадач с пагинацией, фильтрацией, поиском и сортировкой
class SubTaskListCreateView(generics.ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Фильтрация по статусу и дедлайну
        status = self.request.query_params.get('status')
        deadline = self.request.query_params.get('deadline')
        if status:
            queryset = queryset.filter(status=status)
        if deadline:
            queryset = queryset.filter(deadline__lte=deadline)

        # Поиск по title и description
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(title__icontains=search) | queryset.filter(description__icontains=search)

        # Сортировка по created_at
        queryset = queryset.order_by('created_at')

        return queryset


# Представление для получения, обновления и удаления подзадач
class SubTaskDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer


# Представление для категорий с кастомным методом для подсчета задач
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def count_tasks(self, request, pk=None):
        category = self.get_object()
        task_count = Task.objects.filter(category=category).count()
        return Response({'task_count': task_count})

