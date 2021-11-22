from rest_framework.exceptions import ValidationError

from pylib_libs import divided_by_2_3, divided_by_5_7
from apps.prime import exceptions


def is_prime_validate(n: int):
    try:
        divided_by_2_3.utils.validate(n)
        divided_by_5_7.utils.validate(n)
    except exceptions.DividedException as e:
        raise ValidationError(str(e)) from e
