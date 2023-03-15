# Generated by Django 4.1 on 2023-03-15 17:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0011_alter_job_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="program",
            name="artifact",
            field=models.FileField(
                upload_to="artifacts_%Y_%m_%d",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["tar"]
                    )
                ],
            ),
        ),
    ]
