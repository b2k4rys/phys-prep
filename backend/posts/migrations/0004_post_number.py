# Generated by Django 5.1.3 on 2024-11-09 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
