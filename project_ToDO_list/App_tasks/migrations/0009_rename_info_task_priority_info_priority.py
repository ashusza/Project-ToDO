# Generated by Django 4.2.2 on 2023-06-29 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_tasks', '0008_alter_info_task_deadline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='info_task_priority',
            new_name='priority',
        ),
    ]