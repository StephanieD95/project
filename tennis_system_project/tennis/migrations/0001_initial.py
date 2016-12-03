# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-17 15:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tennis.Camp')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('sname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=128)),
                ('emrgcon1', models.CharField(max_length=128)),
                ('emrgcon2', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('sname', models.CharField(max_length=30)),
                ('medicalcons', models.CharField(max_length=128)),
                ('btmno', models.IntegerField()),
                ('dob', models.DateField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tennis.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeofday', models.CharField(max_length=30)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tennis.Day')),
            ],
        ),
        migrations.AddField(
            model_name='attendance',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tennis.Player'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tennis.Session'),
        ),
    ]