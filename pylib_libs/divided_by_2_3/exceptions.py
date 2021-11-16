class DividedException(Exception):
    pass


class DividedBy2Exception(DividedException):
    pass


class DividedBy3Exception(DividedException):
    pass


class DividedBy6Exception(DividedBy2Exception, DividedBy3Exception):
    pass
