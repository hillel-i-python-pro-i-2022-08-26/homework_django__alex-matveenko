# Generated by Django 4.1.1 on 2022-11-05 14:12

from django.db import migrations, models

import phone_book.models


class Migration(migrations.Migration):
    dependencies = [
        ("phone_book", "0007_rename_phonebook_contact"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to=phone_book.models.get_avatar_path),
        ),
    ]