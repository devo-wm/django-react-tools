# Generated by Django 2.1.9 on 2019-06-12 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reacttools', '0002_auto_20190612_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='reactappsettings',
            name='build_path',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
