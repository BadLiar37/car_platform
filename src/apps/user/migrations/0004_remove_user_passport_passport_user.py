# Generated by Django 4.2.7 on 2023-11-28 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_passport_user_passport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='passport',
        ),
        migrations.AddField(
            model_name='passport',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
