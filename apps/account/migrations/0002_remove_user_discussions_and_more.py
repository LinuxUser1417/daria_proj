# Generated by Django 4.2.5 on 2023-09-23 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='discussions',
        ),
        migrations.RemoveField(
            model_name='user',
            name='liked_discussions',
        ),
    ]
