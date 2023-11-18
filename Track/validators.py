from django.forms import ValidationError


def non_negative_validator(value):
    if value < 0:
        raise ValidationError('cannot be negative')
