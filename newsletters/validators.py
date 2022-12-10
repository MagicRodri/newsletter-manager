from django.core.exceptions import ValidationError


def validate_phone_number(number):
    """
        Basic russian number validator
    """
    if not number.startswith('7'):
        raise ValidationError('Phone number must start with 7')
    elif len(number)!=11:
        raise ValidationError('Phone number must contain exactly 11 digits')
    elif not all([x.isdigit() for x in number]):
        raise ValidationError('Phone number must be only digits')