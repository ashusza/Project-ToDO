# Generated by Django 4.2.2 on 2023-07-08 14:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App_tasks', '0014_alter_info_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='task_deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
