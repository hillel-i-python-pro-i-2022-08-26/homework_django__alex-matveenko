# Generated by Django 4.1.1 on 2022-11-23 09:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("phone_book", "0002_contact_delete_phonebook"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contact",
            options={"ordering": ["-create_at"], "verbose_name": "Contact", "verbose_name_plural": "Contacts"},
        ),
    ]
