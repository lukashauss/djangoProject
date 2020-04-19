# Generated by Django 3.0.3 on 2020-04-19 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chess', '0009_remove_chessgame_player2'),
    ]

    operations = [
        migrations.AddField(
            model_name='chessgame',
            name='player2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
