# Generated by Django 2.1.5 on 2019-04-25 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gavin', '0013_remove_article_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
            preserve_default=False,
        ),
    ]
