from django.db import models


class SessionHandler(models.Model):
    session_key = models.CharField(max_length=255)
    path = models.SlugField(max_length=255)
    count_of_visits = models.IntegerField()
    user = models.ForeignKey(
        "admin_users.AdminUser",
        on_delete=models.SET_NULL,
        null=True,
    )
    last_visit_at = models.DateTimeField(auto_now=True)
