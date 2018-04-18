# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-18 06:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-create_time']},
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='publish_time',
            new_name='create_time',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='update_time',
            new_name='last_update_time',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='caption',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='recommend',
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='blog',
            name='tags',
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Tag'),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
