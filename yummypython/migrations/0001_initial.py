# Generated by Django 3.2 on 2021-05-20 07:16

from django.db import migrations, models
import django.db.models.deletion
import django_markdown.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=True, max_length=50, verbose_name='topic')),
            ],
        ),
        migrations.CreateModel(
            name='Subtopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=True, max_length=50, verbose_name='subtopic')),
                ('content', django_markdown.models.MarkdownField(default=True)),
                ('topic', models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='yummypython.topic')),
            ],
        ),
    ]
