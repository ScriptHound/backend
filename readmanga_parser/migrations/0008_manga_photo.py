# Generated by Django 3.1.7 on 2021-03-20 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readmanga_parser', '0007_auto_20210311_0325'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='photo',
            field=models.TextField(blank=True, null=True, verbose_name='url'),
        ),
    ]