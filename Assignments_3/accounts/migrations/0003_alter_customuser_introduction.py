# Generated by Django 4.2 on 2025-01-14 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_customuser_image_customuser_introduction"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="introduction",
            field=models.TextField(blank=True),
        ),
    ]