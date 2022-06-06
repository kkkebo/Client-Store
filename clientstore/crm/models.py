from django.db import models

# Create your models here.


class Order(models.Model):
    order_date = models.DateTimeField(auto_now=True, verbose_name='Дата заказа')
    name = models.CharField(max_length=200, verbose_name='Имя заказчика')
    email = models.EmailField(verbose_name='Эл. почта заказчика')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон заказчика')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-order_date']