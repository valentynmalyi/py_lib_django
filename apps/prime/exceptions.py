from pylib_libs import divided_by_2_3, divided_by_5_7


class DividedException(divided_by_2_3.exceptions.DividedException, divided_by_5_7.exceptions.DividedException):
    pass
