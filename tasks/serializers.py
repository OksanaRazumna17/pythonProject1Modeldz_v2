from rest_framework import serializers
from django.utils import timezone
from .models import Task, SubTask, Category  # Убедись, что ты добавил модель Category

# Сериализатор для создания подзадачи
class SubTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'title', 'description', 'status', 'deadline', 'created_at', 'task']
        read_only_fields = ['created_at']  # Поле только для чтения

# Сериализатор для подзадачи
class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'title', 'description', 'status', 'deadline', 'created_at', 'task']

# Сериализатор для создания задачи с вложенными подзадачами
class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'deadline', 'created_at', 'subtasks']

# Сериализатор для подробного отображения задачи с подзадачами
class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'deadline', 'created_at', 'subtasks']

# Сериализатор для создания задачи с валидацией дедлайна
class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'deadline', 'created_at']

    # Проверка, что дедлайн не в прошлом
    def validate_deadline(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Deadline cannot be in the past.")
        return value

# Сериализатор для создания категории с проверкой уникальности
class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

    # Проверка уникальности названия категории
    def validate_title(self, value):
        if Category.objects.filter(title=value).exists():
            raise serializers.ValidationError("Category with this title already exists.")
        return value

    # Переопределение метода создания
    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    # Переопределение метода обновления
    def update(self, instance, validated_data):
        if 'title' in validated_data:
            instance.title = validated_data['title']
        instance.save()
        return instance



