# Generated by Django 4.1.3 on 2022-12-11 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0010_remove_person_footnote'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media/')),
                ('person', models.ManyToManyField(to='person.person', verbose_name='водитель')),
            ],
            options={
                'verbose_name': 'файл',
                'verbose_name_plural': 'файлы',
                'ordering': ('-id',),
            },
        ),
    ]
