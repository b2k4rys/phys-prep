# Generated by Django 5.1.3 on 2024-11-09 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='answer',
            field=models.IntegerField(default=0),
        ),
    ]
