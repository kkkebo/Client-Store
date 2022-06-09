from django.db import models

# Create your models here.
class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Token')
    tg_chat = models.CharField(max_length=200,verbose_name='chat_id')
    tg_message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.tg_chat

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'
