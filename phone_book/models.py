from django.db import models


class Contacts(models.Model):
    name = models.CharField(max_length=255)
    phone = models.SlugField(max_length=100)
    birthday_date = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_auto_generated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} : {self.birthday_date} : {self.phone}"

    __repr__ = __str__
