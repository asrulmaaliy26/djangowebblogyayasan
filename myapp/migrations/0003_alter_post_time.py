# Generated by Django 3.2.12 on 2024-08-09 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20240808_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.CharField(blank=True, default='09 August 2024', max_length=100),
        ),
    ]
