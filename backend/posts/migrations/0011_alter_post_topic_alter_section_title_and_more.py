# Generated by Django 5.1.3 on 2024-11-23 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_alter_post_topic_alter_section_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(default=3258, on_delete=django.db.models.deletion.CASCADE, to='posts.topic'),
        ),
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(default='PHYS 161', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='section',
            field=models.ForeignKey(default=729, on_delete=django.db.models.deletion.CASCADE, to='posts.section'),
        ),
    ]