from django.core.exceptions import ValidationError
from validate_docbr import CPF


def cpf_validator(value):
    if not CPF().validate(value):
        raise ValidationError(message="CPF inválido.")
