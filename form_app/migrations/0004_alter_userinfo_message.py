# Generated by Django 5.0 on 2024-01-11 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0003_auto_20240111_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='message',
            field=models.CharField(max_length=255),
        ),
    ]
