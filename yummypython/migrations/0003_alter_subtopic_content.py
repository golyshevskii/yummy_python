# Generated by Django 3.2 on 2021-05-27 17:32

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('yummypython', '0002_alter_topic_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtopic',
            name='content',
            field=markdownx.models.MarkdownxField(default=True),
        ),
    ]
