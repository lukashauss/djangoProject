# Generated by Django 3.0.3 on 2020-03-29 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpages', '0011_auto_20200329_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='friends',
        ),
        migrations.AddField(
            model_name='userdata',
            name='friends',
            field=models.TextField(blank=True),
        ),
    ]
