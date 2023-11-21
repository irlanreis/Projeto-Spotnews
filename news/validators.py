from django.core.exceptions import ValidationError


def validate_title(value):
    letters = value.split()

    if len(letters) == 1:
        raise ValidationError('O titulo deve conter pelo menos 2 palavras')
