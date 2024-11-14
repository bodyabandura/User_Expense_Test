from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username
