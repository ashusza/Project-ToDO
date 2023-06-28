# Generated by Django 4.2.2 on 2023-06-28 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_tasks', '0005_remove_info_task_details'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detail',
            options={'ordering': ['-task_priority']},
        ),
        migrations.RenameField(
            model_name='detail',
            old_name='task_status',
            new_name='task_code',
        ),
        migrations.RenameField(
            model_name='detail',
            old_name='task_title',
            new_name='task_priority',
        ),
        migrations.AlterModelTable(
            name='detail',
            table='Detail',
        ),
    ]
