from django.db import models

from user.models import User


class Recommendation(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommended_email = models.EmailField(unique=True, null=False, blank=False)
    has_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.recommended_email
