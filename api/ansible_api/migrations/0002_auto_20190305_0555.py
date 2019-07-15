# Generated by Django 2.1.2 on 2019-03-05 05:55

import common.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ansible_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playbook',
            name='extra_vars',
            field=common.models.JsonDictTextField(blank=True, default={}, null=True, verbose_name='Vars'),
        ),
        migrations.AddField(
            model_name='playbookexecution',
            name='extra_vars',
            field=common.models.JsonDictTextField(blank=True, null=True, verbose_name='Vars'),
        ),
    ]