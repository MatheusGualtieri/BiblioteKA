from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    author = models.CharField(max_length=50)
    sinopse = models.TextField()
    publisher = models.CharField(max_length=150)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    users = models.ManyToManyField(
        "users.User",
        related_name="books",
    )
