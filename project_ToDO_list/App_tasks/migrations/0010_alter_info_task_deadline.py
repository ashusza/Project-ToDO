# Generated by Django 4.2.2 on 2023-06-29 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_tasks', '0009_rename_info_task_priority_info_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='task_deadline',
            field=models.DateTimeField(),
        ),
    ]