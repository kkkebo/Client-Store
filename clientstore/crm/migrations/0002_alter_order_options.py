# Generated by Django 4.0.5 on 2022-06-06 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-order_date'], 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]