# Generated by Django 4.2 on 2023-04-21 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_type',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Тип доставки'),
        ),
    ]
