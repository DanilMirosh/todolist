from django.db import migrations, transaction
from django.utils import timezone


def create_objects(apps, schema_editor):
    # Для загрузки кода моделей используется специальный метод apps.get_model
    # Он позволяет загрузить ровно то состояние модели, которое было на момент применения этой миграции
    # Импортировать настоящие классы – плохая практика
    # так как в будущем вы можете удалить/переименовать эти модели, и тогда у вас будут ошибки импорта

    User = apps.get_model('core', 'User')
    Board = apps.get_model('goals', 'Board')
    BoardParticipant = apps.get_model('goals', 'BoardParticipant')
    GoalCategory = apps.get_model('goals', 'GoalCategory')

    now = timezone.now()

    with transaction.atomic():  # Применяем все изменения одной транзакцией
        for user_id in User.objects.values_list('id', flat=True):  # Для каждого пользователя
            new_board = Board.objects.create(title='Мои Цели', created=now, updated=now)
            BoardParticipant.objects.create(user_id=user_id, board=new_board, role=1, created=now, updated=now)
            GoalCategory.objects.filter(user_id=user_id).update(board=new_board)


class Migration(migrations.Migration):
    dependencies = [
        ('goals', '0003_board_goalcategory_board_boardparticipant'),
    ]

    operations = [
        migrations.RunPython(create_objects)
    ]
