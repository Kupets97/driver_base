# Generated by Django 4.1.3 on 2022-12-11 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0009_person_footnote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='footnote',
        ),
    ]
