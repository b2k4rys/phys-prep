# Generated by Django 5.1.3 on 2024-11-23 22:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_alter_post_topic_alter_topic_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(default=8152, on_delete=django.db.models.deletion.CASCADE, to='posts.topic'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='section',
            field=models.ForeignKey(default=1103, on_delete=django.db.models.deletion.CASCADE, to='posts.section'),
        ),
    ]