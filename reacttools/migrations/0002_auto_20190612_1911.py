# Generated by Django 2.1.9 on 2019-06-12 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reacttools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reactappsettings',
            name='css',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='reactappsettings',
            name='js',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='reactappsettings',
            name='manifest',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
