# Generated by Django 4.1.3 on 2022-12-06 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raiting', '0003_alter_raiting_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raiting',
            name='category',
            field=models.CharField(max_length=10, verbose_name='Категория'),
        ),
    ]
