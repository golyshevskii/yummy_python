# Generated by Django 3.2 on 2021-06-02 10:29

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('playroom', '0002_alter_task_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='content',
            field=martor.models.MartorField(default=True),
        ),
    ]
