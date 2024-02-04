from django.core import exceptions


def validate_count(value):
    if value < 0:
        raise exceptions.ValidationError('价格不能为负数')


def convert_to_bool(value):
    if value in [True, 'True', 'true', 1, '1']:
        return True
    elif value in [False, 'False', 'false', 0, '0']:
        return False
    else:
        raise exceptions.ValidationError('Value must be either True or False.')
