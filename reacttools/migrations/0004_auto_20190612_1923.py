# Generated by Django 2.1.9 on 2019-06-12 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reacttools', '0003_reactappsettings_build_path'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reactappsettings',
            old_name='build_path',
            new_name='project_dir',
        ),
    ]
