def is_divided_by_2(n: int) -> bool:
    if n % 2 == 0:
        return True
    return False


def is_divided_by_3(n: int) -> bool:
    if n % 3 == 0:
        return True
    return False


def is_divided(n: int) -> bool:
    if is_divided_by_2(n):
        return True
    return is_divided_by_3(n)
