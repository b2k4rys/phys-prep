# Generated by Django 5.1.3 on 2024-11-23 20:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_post_body_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[(161, 'PHYS 161'), (162, 'PHYS 162')], default='PHYS 161')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('set_number', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
                ('section', models.ForeignKey(default=1145, on_delete=django.db.models.deletion.CASCADE, to='posts.section')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(default=2820, on_delete=django.db.models.deletion.CASCADE, to='posts.topic'),
        ),
    ]
