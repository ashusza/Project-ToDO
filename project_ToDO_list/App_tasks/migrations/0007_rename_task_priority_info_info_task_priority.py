# Generated by Django 4.2.2 on 2023-06-28 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_tasks', '0006_alter_detail_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='task_priority',
            new_name='info_task_priority',
        ),
    ]
