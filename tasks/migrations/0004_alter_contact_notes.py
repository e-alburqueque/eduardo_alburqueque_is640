# Generated by Django 4.2.7 on 2023-12-05 03:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0003_contact_notes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="notes",
            field=models.TextField(default="", max_length=200),
        ),
    ]
