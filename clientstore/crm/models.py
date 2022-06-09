from django.db import models

# Create your models here.


class Order(models.Model):
    order_date = models.DateTimeField(auto_now=True, verbose_name='Дата заказа')
    name = models.CharField(max_length=200, verbose_name='Имя заказчика')
    email = models.EmailField(verbose_name='Эл. почта заказчика')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон заказчика')
    order_status = models.ForeignKey('StatusCrm', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-order_date']


class StatusCrm(models.Model):
    Status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        return self.Status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class CommentCrm(models.Model):
    com_binding = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='Заявка')
    com_text = models.TextField(verbose_name='Текст комментария')
    com_date = models.DateTimeField(auto_now=True, verbose_name='Дата комментария')

    def __str__(self):
        return self.com_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
