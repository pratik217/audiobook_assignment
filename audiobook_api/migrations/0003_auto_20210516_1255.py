# Generated by Django 2.2 on 2021-05-16 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audiobook_api', '0002_auto_20210516_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobookitem',
            name='duration',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='songitem',
            name='duration',
            field=models.CharField(max_length=255),
        ),
    ]
