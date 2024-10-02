from django.db import models

# Определяем STATUS_CHOICES выше, чтобы он был доступен для обеих моделей
STATUS_CHOICES = [
    ('New', 'New'),
    ('In progress', 'In progress'),
    ('Pending', 'Pending'),
    ('Blocked', 'Blocked'),
    ('Done', 'Done'),
]

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name  # Строковое представление модели

    class Meta:
        db_table = 'task_manager_category'  # Имя таблицы в базе данных
        verbose_name = 'Category'  # Человекочитаемое имя модели
        unique_together = ['name']  # Уникальность по полю 'name'


class Task(models.Model):
    title = models.CharField(max_length=200, unique=True)  # Уникальность по полю 'title'
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='New')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  # Строковое представление модели

    class Meta:
        db_table = 'task_manager_task'  # Имя таблицы в базе данных
        ordering = ['-created_at']  # Сортировка по убыванию даты создания
        verbose_name = 'Task'  # Человекочитаемое имя модели
        unique_together = ['title']  # Уникальность по полю 'title'


class SubTask(models.Model):
    title = models.CharField(max_length=200, unique=True)  # Уникальность по полю 'title'
    description = models.TextField()
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='New')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  # Строковое представление модели

    class Meta:
        db_table = 'task_manager_subtask'  # Имя таблицы в базе данных
        ordering = ['-created_at']  # Сортировка по убыванию даты создания
        verbose_name = 'SubTask'  # Человекочитаемое имя модели
        unique_together = ['title']  # Уникальность по полю 'title'




