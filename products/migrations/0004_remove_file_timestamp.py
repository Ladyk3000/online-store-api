# Generated by Django 4.0.6 on 2022-07-09 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='timestamp',
        ),
    ]
