from django.db import models
from django.utils import timezone
from users.models import User
from rest_framework.exceptions import ValidationError

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.IntegerField(default=1)
    date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=50)

    def clean(self):
        if self.amount < 1:
            raise ValidationError("Amount cannot be less than 1")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
