# Generated by Django 4.1.1 on 2022-11-23 09:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("middlewares", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="VisitHandler",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("session_key", models.CharField(max_length=255)),
                ("path", models.SlugField(max_length=255)),
                ("count_of_visits", models.IntegerField()),
                ("last_visit_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "verbose_name": "Visit Info",
            },
        ),
        migrations.DeleteModel(
            name="SessionHandler",
        ),
    ]