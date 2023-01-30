from django.db import models


class TgUser(models.Model):
    tg_id = models.BigIntegerField(verbose_name='Chat ID')
    username = models.CharField()
