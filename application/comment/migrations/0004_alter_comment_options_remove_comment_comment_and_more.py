# Generated by Django 4.1.3 on 2022-12-06 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_alter_comment_options_alter_comment_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарии.'},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='comments',
            field=models.CharField(default=1, max_length=1000, verbose_name='Комментарии'),
            preserve_default=False,
        ),
    ]
