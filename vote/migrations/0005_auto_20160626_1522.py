# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-26 15:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vote', '0004_auto_20160615_0202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='nom',
        ),
        migrations.AddField(
            model_name='vote',
            name='usager',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
