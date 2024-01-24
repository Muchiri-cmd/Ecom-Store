# Generated by Django 5.0.1 on 2024-01-24 03:04

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_vendor_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="vendor",
            name="cover_image",
            field=models.ImageField(
                default="vendor.jpg", upload_to=core.models.user_dir_path
            ),
        ),
    ]
