from django.db import models

from user.validators import cpf_validator


class User(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    document = models.CharField(
        max_length=11, unique=True, null=False, blank=False, validators=[cpf_validator]
    )
    email = models.EmailField(unique=True, null=False, blank=False)
    birth_date = models.DateField()
    phone = models.CharField(max_length=11, unique=True, null=False, blank=False)
    balance = models.IntegerField()

    def __str__(self):
        return self.name
