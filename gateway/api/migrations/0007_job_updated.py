# Generated by Django 4.2.2 on 2023-07-31 15:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0006_job_env_vars"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
