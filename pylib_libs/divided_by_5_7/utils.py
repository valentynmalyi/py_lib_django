from pylib_libs.divided_by_5_7.exceptions import DividedBy5Exception, DividedBy7Exception


def _validate_by_5(n: int) -> None:
    if n % 5 == 0:
        raise DividedBy5Exception(f"Число {n} делиться на 5")


def _validate_by_7(n: int) -> None:
    if n % 7 == 0:
        raise DividedBy7Exception(f"Число {n} делиться на 7")


def validate(n: int) -> None:
    _validate_by_5(n)
    _validate_by_7(n)
