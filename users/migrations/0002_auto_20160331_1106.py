# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 14:06
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='owner',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='birth_date',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('U', 'unknown'), ('M', 'male'), ('F', 'female')], default='U', max_length=1, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=users.models.upload_to, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, verbose_name='phone number'),
        ),
    ]
