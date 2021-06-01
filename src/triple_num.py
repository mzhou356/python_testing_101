def triple_num(num):
    """Triple a number supplied.
    
    >>> triple_num(1)
    3
    >>> triple_num(0)
    0
    >>> triple_num(-5)
    -15
    """
    if not (isinstance(num, int ) or isinstance(num, float)):
        raise TypeError
    return 3*num