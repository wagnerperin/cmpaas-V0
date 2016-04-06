# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 13:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('gender', models.CharField(choices=[('U', 'Unknow'), ('M', 'Male'), ('F', 'Female')], default='U', max_length=1)),
                ('image', models.ImageField(blank=True, max_length=254, upload_to='photos')),
            ],
        ),
    ]
