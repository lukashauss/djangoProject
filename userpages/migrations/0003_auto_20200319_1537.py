# Generated by Django 3.0.3 on 2020-03-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpages', '0002_auto_20200319_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='profilePic',
            field=models.ImageField(height_field='100', upload_to='userpages', width_field='100'),
        ),
    ]
