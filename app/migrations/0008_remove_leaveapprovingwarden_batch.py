# Generated by Django 2.1.3 on 2018-11-29 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20181118_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaveapprovingwarden',
            name='batch',
        ),
    ]
