from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        (0, "Admin"),
        (1, "User"),
        (2, "Manager"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatars/")
    role = models.IntegerField(choices=ROLE_CHOICES, default=0)

    list_display = ("name", "email", "phone", "role")
    search_fields = ("name", "email", "phone")
    list_filter = "role"

    # override default table name
    # class Meta:
    #     db_table = 'users'

    def __str__(self):
        return f"{self.name} - {self.email}"
