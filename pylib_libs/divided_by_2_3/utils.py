from pylib_libs.divided_by_2_3.exceptions import DividedBy2Exception, DividedBy3Exception


def is_divided_by_2(n: int) -> None:
    if n % 2 == 0:
        raise DividedBy2Exception(f"Число {n} делиться на 2")


def is_divided_by_3(n: int) -> None:
    if n % 3 == 0:
        raise DividedBy3Exception(f"Число {n} делиться на 3")


def is_divided(n: int) -> None:
    is_divided_by_2(n)
    is_divided_by_3(n)
