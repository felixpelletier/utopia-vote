# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 05:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('poids', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='vote',
            name='poids',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.Poids'),
        ),
    ]
