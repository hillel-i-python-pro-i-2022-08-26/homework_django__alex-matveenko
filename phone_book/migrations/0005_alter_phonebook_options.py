# Generated by Django 4.1.1 on 2022-10-15 08:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("phone_book", "0004_alter_phonebook_phone"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="phonebook",
            options={"ordering": ["-create_at"]},
        ),
    ]
