from django.db import models
from django.urls import reverse
from ulid import ULID


def get_avatar_path(instance, filename: str) -> str:
    ulid = ULID()
    _, extension = filename.rsplit(".", maxsplit=1)
    return f"contacts/contact/avatar/{instance.pk}/{ulid.to_uuid()}/{instance.name}_avatar.{extension}"


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=100)
    birthday_date = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_auto_generated = models.BooleanField(default=False)
    avatar = models.ImageField(
        max_length=255,
        blank=True,
        null=True,
        upload_to=get_avatar_path,
    )

    def __str__(self):
        return f"{self.name} : {self.birthday_date} : {self.phone}"

    __repr__ = __str__

    def get_absolute_url(self):
        return reverse(
            "phone_book:update_user",
            kwargs={"pk": self.pk},
        )

    class Meta:
        ordering = ["-create_at"]
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
