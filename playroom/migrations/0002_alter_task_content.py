# Generated by Django 3.2 on 2021-05-30 08:33

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('playroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='content',
            field=markdownx.models.MarkdownxField(default=True),
        ),
    ]