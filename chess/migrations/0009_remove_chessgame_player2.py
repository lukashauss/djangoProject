# Generated by Django 3.0.3 on 2020-04-19 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chess', '0008_auto_20200419_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chessgame',
            name='player2',
        ),
    ]