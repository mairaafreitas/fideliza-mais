from django.db import models

from user.models import User


class Recommendation(models.Model):
    created_date = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="Data de criação"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Usuário Indicador"
    )
    recommended_email = models.EmailField(
        unique=True, null=False, blank=False, verbose_name="Email do Indicado"
    )
    has_accepted = models.BooleanField(
        default=False, verbose_name="Aceitou a indicação?"
    )

    def __str__(self):
        return self.recommended_email
