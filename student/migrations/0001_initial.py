# Generated by Django 4.1.5 on 2023-02-20 18:35

from django.db import migrations, models
import location_field.models.plain
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("city", models.CharField(default=True, max_length=300)),
                (
                    "location",
                    location_field.models.plain.PlainLocationField(max_length=63),
                ),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None, unique=True
                    ),
                ),
                ("resume", models.FileField(upload_to="uploads")),
                ("cover_letter", models.FileField(upload_to="uploads")),
            ],
            options={
                "db_table": "student",
            },
        ),
    ]
