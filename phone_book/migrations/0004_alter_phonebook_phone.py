# Generated by Django 4.1.1 on 2022-10-10 20:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("phone_book", "0003_alter_phonebook_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="phonebook",
            name="phone",
            field=models.CharField(max_length=100),
        ),
    ]