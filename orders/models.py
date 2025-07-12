from django.db import models
from users.models import User


# Create your models here.
class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()
    # one to many relationship
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="orders"
    )

    def __str__(self):
        return f"{self.date} - {self.total_price}$"
