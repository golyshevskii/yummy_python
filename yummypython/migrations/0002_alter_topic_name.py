# Generated by Django 3.2 on 2021-05-20 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yummypython', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(db_index=True, default=True, max_length=50, unique=True, verbose_name='topic'),
        ),
    ]
