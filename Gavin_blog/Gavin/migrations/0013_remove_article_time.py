# Generated by Django 2.1.5 on 2019-04-25 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gavin', '0012_auto_20190425_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='time',
        ),
    ]
