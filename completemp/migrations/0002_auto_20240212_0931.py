# Generated by Django 2.2.13 on 2024-02-12 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('completemp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='std_batch_id',
            new_name='std_batch',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='std_group_id',
            new_name='std_group',
        ),
    ]
