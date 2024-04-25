# Generated by Django 4.2.11 on 2024-04-25 20:42

import api.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0020_remove_program_arguments"),
    ]

    operations = [
        migrations.AddField(
            model_name="program",
            name="image",
            field=models.CharField(blank=True, max_length=511, null=True),
        ),
        migrations.AlterField(
            model_name="program",
            name="artifact",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=api.models.get_upload_path,
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["tar"]
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="program",
            name="entrypoint",
            field=models.CharField(default="main.py", max_length=255),
        ),
    ]
