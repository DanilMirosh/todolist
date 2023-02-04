import logging

from django.conf import settings
from django.core.management import BaseCommand

from todolist.bot.tg.client import TgClient


class Command(BaseCommand):

    def __init__(self):
        super().__init__()
        self.tg_client = TgClient(token=settings.BOT_TOKEN)
        self.logger = logging.getLogger(__name__)
        self.logger.info('Bot start pooling')

    def handle(self, *args, **options):
        offset = 0
        while True:
            res = self.tg_client.get_updates(offset=offset)
            for item in res.result:
                offset = item.update_id + 1
                self.logger.info(item.message)
                self.tg_client.send_message(item.message.chat.id, item.message.text)
