from django.contrib import admin

from todolist.goals.models import GoalCategory, Goal, GoalComment


@admin.register(GoalCategory)
class GoalCategoryAdmin(admin.ModelAdmin):
    """Класс модели для корректного отображения категорий цели в админ панели"""
    list_display = ('id', 'title', 'user', 'is_deleted')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('is_deleted',)
    readonly_fields = ('created', 'updated',)


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    """Класс модели для корректного отображения целей в админ панели"""
    list_display = ('id', 'title', 'user', 'category', 'status', 'priority')
    list_display_links = ('title',)
    search_fields = ('title', 'description')
    list_filter = ('status', 'priority')
    readonly_fields = ('created', 'updated')


@admin.register(GoalComment)
class GoalCommentAdmin(admin.ModelAdmin):
    """Класс модели для корректного отображения комментариев цели в админ панели"""
    list_display = ('id', 'user', 'text')
    list_display_links = ('text',)
    search_fields = ('text',)
    readonly_fields = ('created', 'updated')
