# Generated by Django 2.1.5 on 2019-04-25 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gavin', '0008_auto_20190425_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='telephone',
        ),
    ]