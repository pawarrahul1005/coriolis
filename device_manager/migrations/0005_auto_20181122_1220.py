# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-22 12:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_manager', '0004_device_user_device'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='u_perm',
            new_name='u_perms',
        ),
    ]