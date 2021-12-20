from django.db import models
from django.db.models.fields import EmailField


class User(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    document = models.CharField(max_length=11, unique=True, null=False, blank=False)
    email = EmailField(unique=True, null=False, blank=False)
    birth_date = models.DateField()
    phone = models.CharField(max_length=11, unique=True, null=False, blank=False)
    balance = models.IntegerField()

    def __str__(self):
        return self.name
