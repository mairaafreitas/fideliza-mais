from django.core.validators import MinLengthValidator
from django.db import models

from user.validators import cpf_validator


class User(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False, verbose_name="Nome")
    document = models.CharField(
        max_length=11,
        unique=True,
        null=False,
        blank=False,
        validators=[cpf_validator],
        verbose_name="CPF",
    )
    email = models.EmailField(
        unique=True, null=False, blank=False, verbose_name="Email"
    )
    birth_date = models.DateField(verbose_name="Data de Nascimento")
    phone = models.CharField(
        max_length=11,
        unique=True,
        null=False,
        blank=False,
        validators=[MinLengthValidator(11)],
        verbose_name="Celular",
    )
    balance = models.IntegerField(verbose_name="Pontuação", default=0)

    def __str__(self):
        return self.name
