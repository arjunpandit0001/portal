# Generated by Django 2.0 on 2020-08-21 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20200821_1119'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='students',
            new_name='student_data',
        ),
    ]
