from django.db import models

from todolist.core.models import User


class BaseModel(models.Model):
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата последнего обновления', auto_now=True)

    class Meta:
        abstract = True


class GoalCategory(BaseModel):
    """Класс модели категорий целей"""
    title = models.CharField(verbose_name='Название', max_length=255)
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.PROTECT)
    is_deleted = models.BooleanField(verbose_name='Удалена', default=False)

    class Meta:
        """Мета-класс для корректного отображение названия модели в админ панели"""
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Goal(BaseModel):
    """Класс модели целей"""

    class Status(models.IntegerChoices):
        """Класс модели для выбора статуса цели"""
        to_do = 1, 'К выполнению'
        in_progress = 2, 'В процессе'
        done = 3, 'Выполнено'
        archived = 4, 'Архив'

    class Priority(models.IntegerChoices):
        """Класс модели для выбора приоритета цели"""
        low = 1, 'Низкий'
        medium = 2, 'Средний'
        high = 3, 'Высокий'
        critical = 4, 'Критический'

    title = models.CharField(verbose_name='Название', max_length=200)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    category = models.ForeignKey(to=GoalCategory, verbose_name='Категория', on_delete=models.RESTRICT,
                                 related_name='goals')
    status = models.PositiveSmallIntegerField(verbose_name='Статус', choices=Status.choices, default=Status.to_do)
    priority = models.PositiveSmallIntegerField(verbose_name='Приоритет', choices=Priority.choices,
                                                default=Priority.medium)
    due_date = models.DateField(verbose_name='Дата выполнения', null=True, blank=True)
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.PROTECT, related_name='goals')

    class Meta:
        """Мета-класс для корректного отображение названия модели в админ панели"""
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'

    def __str__(self):
        return self.title


class GoalComment(BaseModel):
    """Класс модели комментариев цели"""
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор', related_name='comments')
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, verbose_name='Цель', related_name='comments')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        """Мета-класс для корректного отображение названия модели в админ панели"""
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
